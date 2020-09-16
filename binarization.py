
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

