# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：test01.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/12/4 14:38 
"""
import pytesseract
from PIL import Image

def OCR_demo():
    # 导入OCR安装路径，如果设置了系统环境，就可以不用设置了
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # 打开要识别的图片

    # image = Image.open('Snipaste_2020-11-13_12-11-16.png')
    image = Image.open('IMG01/1.jpg')
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image, lang='chi_sim')

    print(text)


if __name__ == '__main__':
    OCR_demo()
