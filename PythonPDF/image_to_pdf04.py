# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：image_to_pdf03.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/10/7 15:03 
"""

from PyPDF2 import PdfWriter, PdfReader
'''
知道需要将哪个图片进行翻转, 记住相应的序号
'''

def page_rotation(old_file, new_file):
    """
    PDF页面旋转
    :param old_file: 需要旋转的PDF文件
    :param new_file: 旋转后的PDF文件
    :return:
    """
    pdf = PdfReader(old_file)
    page_num = len(pdf.pages)
    pdf_writer = PdfWriter()
    # ls1 = [27, 29, 31, 33, 35, 37, 39, 41, 71]
    # ls2 = [35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73]
    # 使用列表生成器来生成以上列表
    ls1 = [x for x in range(27, 43, 2)]
    ls1.append(71)
    ls2 = [x for x in range(35, 74, 2)]
    ls1.extend(ls2)

    for i in range(page_num):
        # orientation = pdf.getPage(i).get('/Rotate')   # 获取页面的旋转角度
        size = pdf.pages[i].mediabox  # 获取页面大小值（长、宽）
        x, y = size.right, size.top
        if i in ls1:
            # 顺时针旋转90度  90的倍数
            page = pdf.pages[i].rotate(180)
            # 逆时针旋转90度  90的倍数
            # page = pdf.pages[i].rotate(90)
            pdf_writer.add_page(page)
        else:
            # 不旋转
            page = pdf.pages[i].rotate(0)
            pdf_writer.add_page(page)
    with open(new_file, 'wb') as f:
        pdf_writer.write(f)


if __name__ == '__main__':
    page_rotation("E:\\BaiduyunDownload\\和研扫描\\1.pdf", "E:\\BaiduyunDownload\\和研扫描\\12.pdf")
