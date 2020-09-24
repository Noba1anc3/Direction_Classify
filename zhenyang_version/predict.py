# from tensorflow.keras.models import load_model
# import tensorflow as tf
# import os
# import math
# import os.path as osp
# import numpy as np
# import tensorflow.keras.backend as K
#
#
# def cosloss(y_true, y_pred):
#     y_true = tf.Print(y_true, ['y_true: ', y_true])
#     y_pred2 = y_pred * 2. * math.pi
#     y_pred2 = tf.Print(y_pred2, ['y_pred: ', y_pred2])
#     loss = K.mean(2. * (1. - tf.cos(0.5 * (y_pred2 - y_true))))
#     loss = tf.Print(loss, ['my loss: ', loss])
#     return loss
#
#
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#
# # 路径参数
# h5_dir = '/home/ubuntu/cs/table_derection_tf2/use_cos_loss/saved_model'
# h5_file = 'model_51.hdf5'
# h5_file_path = osp.join(h5_dir, h5_file)
#
# # 加载模型
# h5_model = load_model(h5_file_path,  custom_objects={'cosloss': cosloss})
#
# # image_input = np.zeros((600, 600, 3))
# # image_input = np.expand_dims(image_input, 0)
# image_input = np.random.rand(1, 600, 600, 3)
# print(h5_model.predict(image_input))
#

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

def global_threshold_demo(image):
    '''二值化'''
    # 1.灰度化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # 2.计算直方图
    hist = cv.calcHist([gray], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # 二值化，ret代表阈值，binary是二值图像
    # cv.THRESH_OTSU,cv.THRESH_TRIANGLE 计算阈值的方法，加上竖线，自动寻找阈值
    ret, binary = cv.threshold(gray, 100, 255, cv.THRESH_TOZERO)  # 100,<100的全部变成0
    print('ret:', ret)
    cv.imshow('binary', binary)


def local_threshold_demo(image):
    """局部自适应二值化"""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # pram:[gray,max_value,local_binary_method,binary_method,blocksize：奇数必须，value-mean>10?white:black]

    # GAUSSIAN_C方法，采用高斯，区域中的（x,y）周围的像素根据高斯函数按照它们离中心点的距离进行加权计算
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)

    return dst


image_dir = 'test/test_image/'

for file in sorted(os.listdir(image_dir)):
    src = cv.imread(image_dir + file)
    cv.imshow('src', src)

    # global_threshold_demo(src)#全局二值化
    dst = local_threshold_demo(src)  # 局部二值化

    #cv.imshow('local_binary', dst)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    cv.imwrite(image_dir + file, dst)
