# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 18:57
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
''''
删除文件/ 删除文件夹
# 1. os.remove     删除文件
# 2. shutil.rmtree 删除文件夹

# 程序删除不去回收站
'''

import os
import shutil

if __name__ == '__main__':
    # os.remove(r'E:\PythonProject\Day17\move_1.jpg')
    # os.removedirs(r'E:\PythonProject\Day17\copy_OnlineLearning') # 该方法只能删除空文件夹
    shutil.rmtree(r'E:\PythonProject\Day17\f1')


