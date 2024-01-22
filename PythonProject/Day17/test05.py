# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 18:41
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
1. shutil.copy()        文件复制
2. shutil.copytree()    文件夹复制 

流 stream => inputstream & outputstream
'''

import shutil

if __name__ == '__main__':
    # src -> source   dest -> destination 目的地
    src = r'E:\PythonProject\Day17\test01.py'
    # dest = r'E:\PythonProject\Day17\f1\copy_test01.py'
    dest = r'copy_test01.py'
    shutil.copy(src, dest)



