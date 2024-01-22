# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：CSV_write.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/8 9:57 
"""
import csv
import pandas as pd

# 写入CSV文件
with open('data/data_write1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

# 使用newline=''防止额外的换行符,delimiter=" "指定用空格代替逗号作为分隔符
with open('data/data_write2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=" ")
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

# writerows， 二维列表
with open('data/data_write3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', '20'], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

# 爬虫爬取的都是结构化数据，一般用字典表示这种数据
with open('data/data_write4.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# 追加模式'a', 编码格式
with open('data/data_write4.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10004', 'name': 'Zhui', 'age': 20})
    writer.writerow({'id': '10005', 'name': '王小鱼', 'age': 20})

data = [
    {'id': '10001', 'name': 'Mike', 'age': 20},
    {'id': '10002', 'name': 'Bob', 'age': 22},
    {'id': '10003', 'name': 'Jordan', 'age': 21},
    {'id': '10005', 'name': '王小鱼', 'age': 20}
]

df = pd.DataFrame(data)
df.to_csv('data/data_write5.csv', index=False)