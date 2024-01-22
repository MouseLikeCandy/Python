# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：CSV_read.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/8 10:37 
"""
import csv
import pandas as pd

# 读取csv文件, Reader对象
with open('data/data_write5.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# DataFrame对象
df = pd.read_csv('data/data_write5.csv')
print(df)

# 进一步转化为列表
data = df.values.tolist()
print(data)

# 直接对df进行遍历得到列表
for index, row in df.iterrows():
    print(row.tolist())

