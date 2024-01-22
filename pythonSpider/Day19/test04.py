# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 20:28
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
csv的第二种写入方式   字典
'''
import csv

if __name__ == '__main__':
    with open('stus2.csv', mode='wt', encoding='utf-8', newline='') as f:
        # 1. 创建一个 CSV writer 对象, 字典的 key 在 CSV 文件格式中称为 fieldnames 属性名称
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'score'])
        # 2. 首先要写入表头
        writer.writeheader()
        # 3. 写入数据
        data_list = [
            {'name': '张三', 'age': 18, 'score': 88},
            {'name': '李四', 'age': 19, 'score': 99},
            {'name': '王五', 'age': 20, 'score': 100},
        ]

        writer.writerows(data_list)
