# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 18:53
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
移动/剪切
# shutil.move() 移动
'''

import shutil

if __name__ == '__main__':
    src = r'E:\PythonProject\Day17\copy_OnlineLearning\1.jpg'
    dest = r'E:\PythonProject\Day17\move_1.jpg'
    shutil.move(src, dest)
    # 移动中给名称, 可以重命名