# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 20:16
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
CSV文件
Comma Separeted Values 逗号分隔符   .csv

csv的第一种写入方式   列表
'''

import csv

if __name__ == '__main__':
    # 数据写入
    # 说明：如果将 f 文件对象和 CSV 对象关联，数据写入后，每行数据之后会多出一个空行，需要使用newline=''这个关键字解决
    with open('stus.csv', mode='wt', encoding='utf-8', newline='') as f:
        # 1. 创建一个 csv writer对象
        writer = csv.writer(f)
        # 2. 一次写入一条数据, 每一行数据都是列表类型
        writer.writerow(['姓名', '年龄', '成绩'])
        # 3. 一次写入多行数据  列表嵌套列表
        data_list = [
            ['张三', 18, 88],
            ['李四', 19, 99],
            ['王五', 20, 100],
        ]
        writer.writerows(data_list)