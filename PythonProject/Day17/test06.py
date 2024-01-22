# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 18:47
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
文件夹复制
'''

import shutil


if __name__ == '__main__':
    # 文件夹
    src = r'E:\PythonProject\OnlineLearning\spider_img'
    dest = r'E:\PythonProject\Day17\copy_OnlineLearning'
    shutil.copytree(src, dest)



