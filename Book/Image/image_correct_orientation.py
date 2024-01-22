# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：image_correct_orientation.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/11/27 9:08 
"""

'''
# 怎样将图片中的图片摆正
'''
import cv2
import numpy as np

def correct_orientation(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用Canny边缘检测
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # 寻找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 寻找最大的轮廓
    largest_contour = max(contours, key=cv2.contourArea)

    # 计算最小外接矩形
    rect = cv2.minAreaRect(largest_contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 计算旋转角度
    angle = rect[-1]

    # 旋转图像
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # 显示原始图像和矫正后的图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Corrected Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "F.png"
    correct_orientation(image_path)
