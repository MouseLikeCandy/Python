# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 18:13
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
os.walk()   游历
类似于递归的操作, 如果发现文件夹, 一层层进入取出内容
'''

import os

if __name__ == '__main__':
    path =  r'D:\CommonSoft\WeChat\documents\WeChat Files\All Users'
    directory_tree_generator = os.walk(path)
    # generator 生成器对象(可遍历)
    print(directory_tree_generator)
    # dirpath, dirnames, filenames -> 包装为一个元组
    # 根目录, 文件夹, 文件名
    # for element in directory_tree_generator:
    #     print(element)
    print('-' * 100)

    for dirpath, dirnames, filenames in directory_tree_generator:
        # 需求: 获取所有的.jpg文件
        # print(dirpath)
        # print(dirnames)
        # print(filenames)
        # print('-' * 100)

        # 判断: filenames 是列表
        for filename in filenames:
            # filename 是字符串. startswith() 以什么开始   endswith() 以什么结尾
            if filename.endswith('.jpg'):
                # 1. 打印文件名
                print(filename)
                # 2. 输出查看该文件的绝对路径, 能够区分不同文件夹下的同名文件
                abspath = dirpath + '\\' + filename
                print(abspath)
                abspath = os.path.join(dirpath, filename)
                print(abspath)

        print('-' * 100)



