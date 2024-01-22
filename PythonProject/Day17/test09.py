# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 19:01
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
重命名
# os.rename()
'''

import  os

if __name__ == '__main__':
    src = r'E:\PythonProject\Day17\2.jpg'
    dest = r'E:\PythonProject\Day17\rename_2.jpg'
    os.rename(src, dest)
