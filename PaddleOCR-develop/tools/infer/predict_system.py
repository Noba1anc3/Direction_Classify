# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../..')))

import tools.infer.utility as utility
from ppocr.utils.utility import initial_logger

logger = initial_logger()
import cv2
from tools.infer.correct import angle_correction
import tools.infer.predict_det as predict_det
import tools.infer.predict_cls as predict_cls
import copy
import numpy as np
import math
from ppocr.utils.utility import get_image_file_list, check_and_read_gif


class TextSystem(object):
    def __init__(self, args):
        self.text_detector = predict_det.TextDetector(args)
        self.use_angle_cls = args.use_angle_cls
        if self.use_angle_cls:
            self.text_classifier = predict_cls.TextClassifier(args)

    def cal_ver_hor_edge(self, dt_box):
        """
        :param dt_box: a list of four points
        :return: the vertical and horizonal edge length of the dt_box
        """
        if dt_box[1][0] - dt_box[0][0] == 0:
            line_up = 90
        else:
            line_up = (dt_box[1][1] - dt_box[0][1]) / (dt_box[1][0] - dt_box[0][0])
            line_up = math.fabs(int(math.atan(line_up) * 180 / math.pi))
        if dt_box[2][0] - dt_box[1][0] == 0:
            line_rt = 90
        else:
            line_rt = (dt_box[2][1] - dt_box[1][1]) / (dt_box[2][0] - dt_box[1][0])
            line_rt = math.fabs(int(math.atan(line_rt) * 180 / math.pi))
        if dt_box[3][0] - dt_box[2][0] == 0:
            line_dn = 90
        else:
            line_dn = (dt_box[3][1] - dt_box[2][1]) / (dt_box[3][0] - dt_box[2][0])
            line_dn = math.fabs(int(math.atan(line_dn) * 180 / math.pi))
        if dt_box[0][0] - dt_box[3][0] == 0:
            line_lt = 90
        else:
            line_lt = (dt_box[0][1] - dt_box[3][1]) / (dt_box[0][0] - dt_box[3][0])
            line_lt = math.fabs(int(math.atan(line_lt) * 180 / math.pi))

        if line_up <= min(line_rt, line_dn, line_lt):
            horizonal_edge = math.sqrt(pow(dt_box[0][0] - dt_box[1][0], 2) + pow(dt_box[0][1] - dt_box[1][1], 2))
        elif line_rt <= min(line_up, line_dn, line_lt):
            horizonal_edge = math.sqrt(pow(dt_box[2][0] - dt_box[1][0], 2) + pow(dt_box[2][1] - dt_box[1][1], 2))
        elif line_dn <= min(line_rt, line_up, line_lt):
            horizonal_edge = math.sqrt(pow(dt_box[2][0] - dt_box[3][0], 2) + pow(dt_box[2][1] - dt_box[3][1], 2))
        elif line_lt <= min(line_rt, line_dn, line_up):
            horizonal_edge = math.sqrt(pow(dt_box[0][0] - dt_box[3][0], 2) + pow(dt_box[0][1] - dt_box[3][1], 2))

        if line_up >= max(line_rt, line_dn, line_lt):
            vertical_edge = math.sqrt(pow(dt_box[0][0] - dt_box[1][0], 2) + pow(dt_box[0][1] - dt_box[1][1], 2))
        elif line_rt >= max(line_up, line_dn, line_lt):
            vertical_edge = math.sqrt(pow(dt_box[2][0] - dt_box[1][0], 2) + pow(dt_box[2][1] - dt_box[1][1], 2))
        elif line_dn >= max(line_rt, line_up, line_lt):
            vertical_edge = math.sqrt(pow(dt_box[2][0] - dt_box[3][0], 2) + pow(dt_box[2][1] - dt_box[3][1], 2))
        elif line_lt >= max(line_rt, line_dn, line_up):
            vertical_edge = math.sqrt(pow(dt_box[0][0] - dt_box[3][0], 2) + pow(dt_box[0][1] - dt_box[3][1], 2))

        return vertical_edge, horizonal_edge

    def get_rotate_crop_image(self, img, dt_box):
        """
        img_height, img_width = img.shape[0:2]
        left = int(np.min(points[:, 0]))
        right = int(np.max(points[:, 0]))
        top = int(np.min(points[:, 1]))
        bottom = int(np.max(points[:, 1]))
        img_crop = img[top:bottom, left:right, :].copy()
        points[:, 0] = points[:, 0] - left
        points[:, 1] = points[:, 1] - top
        """

        vertical_edge, horizonal_edge = self.cal_ver_hor_edge(dt_box)

        img_crop_width = int(
            max(
                np.linalg.norm(dt_box[0] - dt_box[1]),
                np.linalg.norm(dt_box[2] - dt_box[3])))
        img_crop_height = int(
            max(
                np.linalg.norm(dt_box[0] - dt_box[3]),
                np.linalg.norm(dt_box[1] - dt_box[2])))

        pts_std = np.float32([[0, 0], [img_crop_width, 0],
                              [img_crop_width, img_crop_height],
                              [0, img_crop_height]])
        M = cv2.getPerspectiveTransform(dt_box, pts_std)
        dst_img = cv2.warpPerspective(
            img,
            M, (img_crop_width, img_crop_height),
            borderMode=cv2.BORDER_REPLICATE,
            flags=cv2.INTER_CUBIC)

        dst_img_height, dst_img_width = dst_img.shape[0:2]
        if dst_img_height * 1.0 / dst_img_width >= 1.5:
            dst_img = np.rot90(dst_img)

        Wrong_Perspective = False
        if img_crop_height / img_crop_width < 1 and vertical_edge / horizonal_edge > 1:
            Wrong_Perspective = True
        elif img_crop_height / img_crop_width > 1 and vertical_edge / horizonal_edge < 1:
            Wrong_Perspective = True

        WH_Ratio = False
        dst_img_height, dst_img_width = dst_img.shape[0:2]
        if dst_img_width * 1.0 / dst_img_height > 2:
            WH_Ratio = True

        return dst_img, Wrong_Perspective, WH_Ratio

    def __call__(self, img):
        print("Image Rotation")
        img, elapse = angle_correction(img)
        with open('result.txt', 'a+') as f:
            f.write(' ' + '%.2f' % (elapse * 1000))

        print("   Elapsed : {}ms"
              .format('%.2f' % (elapse * 1000)))
        ori_im = img.copy()

        print("Text Detection")
        dt_boxes, elapse = self.text_detector(img)

        with open('result.txt', 'a+') as f:
            f.write(' ' + '%.2f' % (elapse * 1000))
        print("   Boxes Num : {}\n   Elapsed : {}ms"
              .format(len(dt_boxes), '%.2f' % (elapse * 1000)))

        mid_time = time.time()

        left_right = up_down = 0
        for dt_box in dt_boxes:
            vertical_edge, horizonal_edge = self.cal_ver_hor_edge(dt_box)

            if horizonal_edge < vertical_edge:
                left_right += vertical_edge / horizonal_edge
            else:
                up_down += horizonal_edge / vertical_edge
        print('UD - LR\n   UD Score :', '%.2f' % up_down, '\n   LR Score :', '%.2f' % left_right)

        print('Intermidiate Filter')
        if dt_boxes is None:
            return 0
        dt_boxes = sorted_boxes(dt_boxes)
        for i, dt_box in enumerate(dt_boxes):
            vertical_edge, horizonal_edge = self.cal_ver_hor_edge(dt_box)
            if up_down > left_right and vertical_edge / horizonal_edge > 1:
                del dt_boxes[i]
                print('   Filter Reversed WH-Ratio Boxes')
            elif up_down <= left_right and vertical_edge / horizonal_edge < 1:
                del dt_boxes[i]
                print('   Filter Reversed WH-Ratio Boxes')

        img_crop_list = []
        for bno in range(len(dt_boxes)):
            tmp_box = copy.deepcopy(dt_boxes[bno])
            img_crop, wrong_perspective, wh_ratio = self.get_rotate_crop_image(ori_im, tmp_box)
            if wh_ratio:
                img_crop_list.append(img_crop)
            else:
                print('   Filter Low WH-Ratio Boxes')

        with open('result.txt', 'a+') as f:
            f.write(' ' + '%.2f' % ((time.time() - mid_time) * 1000))
        print("   Remained Boxes Num : {}\n   Elapsed : {}ms".format(
            len(img_crop_list), '%.2f' % ((time.time() - mid_time) * 1000)))

        print('Direction Classification')
        if self.use_angle_cls:
            img_crop_list, angle_list, elapse, lr = self.text_classifier(
                img_crop_list[:10])

            with open('result.txt', 'a+') as f:
                f.write(' ' + '%.2f' % (elapse * 1000))
            print("   Used Boxes Num : {}\n   Elapsed : {}ms".format(
                len(img_crop_list), '%.2f' % (elapse * 1000)))

            with open('result.txt', 'a+') as f:
                if left_right >= up_down and lr == 1:
                    print('Final Direction : Right\n')
                    f.write(' ' + str(3) + '\n')
                    return 3
                elif left_right >= up_down and lr == 0:
                    print('Final Direction : Left\n')
                    f.write(' ' + str(1) + '\n')
                    return 1
                elif left_right < up_down and lr == 1:
                    print('Final Direction : Up\n')
                    f.write(' ' + str(0) + '\n')
                    return 0
                elif left_right < up_down and lr == 0:
                    print('Final Direction : Down\n')
                    f.write(' ' + str(2) + '\n')
                    return 2


def sorted_boxes(dt_boxes):
    """
    Sort text boxes in order from top to bottom, left to right
    args:
        dt_boxes(array):detected text boxes with shape [4, 2]
    return:
        sorted boxes(array) with shape [4, 2]
    """
    num_boxes = dt_boxes.shape[0]
    sorted_boxes = sorted(dt_boxes, key=lambda x: (x[0][1], x[0][0]))
    _boxes = list(sorted_boxes)

    for i in range(num_boxes - 1):
        if abs(_boxes[i + 1][0][1] - _boxes[i][0][1]) < 10 and \
                (_boxes[i + 1][0][0] < _boxes[i][0][0]):
            tmp = _boxes[i]
            _boxes[i] = _boxes[i + 1]
            _boxes[i + 1] = tmp
    return _boxes


def main(args):
    image_file_list = get_image_file_list(args.image_dir)
    text_sys = TextSystem(args)
    for image_file in sorted(image_file_list):

        with open('result.txt', 'a+') as f:
            f.write(image_file.split('images/')[1])
        print(image_file.split('images/')[1])

        img, flag = check_and_read_gif(image_file)
        if not flag:
            img = cv2.imread(image_file)
        if img is None:
            logger.info("error in loading image:{}".format(image_file))
            continue
        text_sys(img)


if __name__ == "__main__":
    main(utility.parse_args())
