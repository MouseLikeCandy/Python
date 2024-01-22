# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 19:16
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
案例: 复制一张图片到当前项目的images文件夹下, 如果images文件夹不存在,
        就先创建文件夹, 然后实现复制.
'''

import os
import shutil

if __name__ == '__main__':
    src = r'E:\PythonProject\Day17\images\teacher_cang4.jpg'
    # dest = r'_images\copy_teacher_cang5.jpg'

    # 判断_images文件夹是否存在
    if not os.path.exists('_images'):
        print('创建_images文件夹...')
        os.makedirs('_images')

    shutil.copy(src, '_images')


