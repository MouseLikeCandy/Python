# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：image_to_pdf.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/10/7 14:25 
"""
from PIL import Image
import os


def jpg2pdf(jpgFile):
    global imglist

    path, fileName = jpgFile.rsplit('\\', 1)
    preName, postName = fileName.rsplit('.', 1)

    img = Image.open(jpgFile)
    imglist.append(img)
    return img.save(path + "\\" + preName + '.pdf', "PDF", resolution=100.0, save_all=True)


def jpg2pdfByPath(pathName):
    global imglist

    imglist = []
    imgfile = ''
    files = os.listdir(pathName)
    for f in files:
        if f.lower().find(".jpg") > 0:
            # jpg2pdf(pathName + '\\' + f)
            img = Image.open(pathName + '\\' + f)
            imglist.append(img)
            imgfile = f

    imgMerge = imglist.pop(0)  # 取出第一个图片示例

    imgMerge.save(pathName + r'\merge.pdf', "PDF", resolution=100.0, save_all=True, append_images=imglist)
    print("all images processed!")


# jpg2pdfByPath(r'E:\BaiduyunDownload\说明书')
jpg2pdfByPath(r'E:\BaiduyunDownload\和研扫描')
