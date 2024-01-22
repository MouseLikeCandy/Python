# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 18:04
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
需求: 获取指定目录下的所有.py文件.(相对路径)
'''

import  os
if __name__ == '__main__':
    # 路径:
    # 相对路径: 当前工作目录
    # 绝对路径: 拥有根盘符的路径
    # current working directory
    path = os.getcwd()
    print(path)

    # listdir 列举目录
    listdir = os.listdir(path)
    print(listdir)

    for filename in listdir:
        print(filename)