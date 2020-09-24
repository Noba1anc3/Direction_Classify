import os
import numpy as np
import tensorflow as tf
import random
import cv2
import time
from tensorflow.keras.mixed_precision import experimental as mixed_precision


def dataloder(img_root):
    img_paths = []
    for path in sorted(os.listdir(img_root)):
        img_path = os.path.join(img_root, path)
        img_paths.append(img_path)
    return img_paths


def decode_and_resize(filename):
    image_string = tf.io.read_file(filename)  # 读取原始文件
    image_decoded = tf.image.decode_jpeg(image_string)  # 解码JPEG图片!!! 解码png时出现通道数错误！！！
    image_resized = tf.image.resize(image_decoded, [600, 600]) / 255.0

    return image_resized, filename


# def test_show(filepath, angle, label):
#     filepath = filepath.decode('utf-8')
#     image = cv2.imread(filepath)
#     h, w = image.shape[:2]
#     c_w, c_h = w//2, h//2
#     n_w, n_h = int((w * 0.6)/2), int((h * 0.6)/2)
#     crop_img = image[c_h-n_h:c_h+n_h, c_w-n_w:c_w+n_w]
#     resized = cv2.resize(crop_img, (600, 600))
#     # rotated = rotate_bound(resized, -angle)
#     cv2.imwrite('./wrong_images/{}'.format(str(angle)+'_'+str(label)+'.jpg'), resized)#rotated)


if __name__ == '__main__':
    batch_size = 1
    model = tf.saved_model.load('./pb/')
    img_root = './test/test_image'

    # 数据加载
    test_filenames = dataloder(img_root)
    test_filenames = tf.constant(test_filenames)
    test_dataset = tf.data.Dataset.from_tensor_slices((test_filenames))
    test_dataset = test_dataset.map(
        map_func=decode_and_resize,
        num_parallel_calls=tf.data.experimental.AUTOTUNE)

    test_dataset = test_dataset.batch(batch_size)
    test_dataset = test_dataset.prefetch(tf.data.experimental.AUTOTUNE)

    cnt = 0
    correct = 0
    sum_time = 0
    count = 0

    with open('pred.txt', 'r') as f:

        for step, (images, filename) in enumerate(test_dataset):
            count += 1
            start = time.time()
            pre_angles = model(images)
            end = time.time()
            sum_time += (end - start)

            preds = pre_angles.numpy()
            preds = preds * 360.0
            path = filename.numpy()
            print(count)
            f.write(str(path) + '\t' + str(preds) + '\n')
        #     for i, pred in enumerate(preds):
        #         cnt += 1
        #         if abs(pred[0] - 0.0) <= 20:
        #             correct += 1
        #         # else:
        #         print('pre_angle: ', pred[0])
        #         print('filename: ', path[i])
        #
        # print('#' * 30)
        # print('correct:{}/{}'.format(correct, cnt))
        # print('acc: ', correct / cnt)
        # print('pre_time: ', sum_time / count)
