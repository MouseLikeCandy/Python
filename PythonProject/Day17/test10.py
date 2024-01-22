# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 19:04
@Auth ： 异世の阿银
@File ：test10.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
批量重命名
'''
import os

if __name__ == '__main__':
    path = r'E:\PythonProject\Day17\images'
    # 遍历文件夹中的所有文件
    listdir = os.listdir(path)
    num = 0
    # 需要获取文件名的绝对路径
    for filename in listdir:
        num += 1
        src = os.path.join(path, filename)
        dest = os.path.join(path, f'teacher_cang{num}.jpg')
        os.rename(src, dest)
