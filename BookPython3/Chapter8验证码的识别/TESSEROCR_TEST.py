# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：TESSEROCR_TEST.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/23 15:32 
"""
import tesserocr
from PIL import Image
import numpy as np

'''
感觉没有合理解决 tessdata 路径的问题
'''

image = Image.open('image/captcha.png')
result = tesserocr.image_to_text(image)
print('第一张图片：', result)
print('第二张图片：', tesserocr.file_to_text('image/captcha2.png'))
print(np.array(image).shape)
print(image.mode)

# 转为灰度图像
image = image.convert('L')
# image.show()

# 二值化
image = image.convert('1')
# image.show()

image = Image.open('image/captcha.png')
image = image.convert('L')
threshold = 50
array = np.array(image)
array = np.where(array > threshold, 255, 0)
image = Image.fromarray(array.astype('uint8'))
image.show()
print('重新识别第一张图片：', tesserocr.image_to_text(image))
