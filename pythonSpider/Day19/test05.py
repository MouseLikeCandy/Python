# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 20:37
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
读取csv
newline='' 读取数据时可以不添加
第一种读取方式
'''
import csv


if __name__ == '__main__':
    with open('stus.csv', mode='rt', encoding='utf-8', newline='') as f:
        # 1. 创建一个 csv 文件读取对象
        reader = csv.reader(f)
        # 2. reader对象可以直接遍历
        for row in reader:
            print(row)