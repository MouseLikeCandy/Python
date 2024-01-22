# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：image_to_pdf03.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/10/7 15:03 
"""

from PyPDF2 import PdfWriter, PdfReader


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
    for i in range(page_num):
        # orientation = pdf.getPage(i).get('/Rotate')   # 获取页面的旋转角度
        size = pdf.pages[i].mediabox  # 获取页面大小值（长、宽）
        x, y = size.right, size.top
        if x > y:
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