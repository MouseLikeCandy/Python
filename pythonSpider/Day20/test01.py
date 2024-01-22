# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/12 10:44
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from pymongo import MongoClient

# 获取连接的客户端
client = MongoClient(host='localhost', port=27017)

# 获取student数据库
db = client['student']

# 获取集合
collection = db['exam']

# 插入数据
stu_list = [
    # {'name': '关羽', 'chinese': 85, 'math': 76, 'english': 60},
    # {'name': '张飞', 'chinese': 70, 'math': 75, 'english': 70},
    # {'name': '赵云', 'chinese': 90, 'math': 65, 'english': 95},
    # {'name': '刘备', 'chinese': 97, 'math': 50, 'english': 50},
    # {'name': '曹操', 'chinese': 90, 'math': 89, 'english': 80},
    # {'name': '司马懿', 'chinese': 90, 'math': 67, 'english': 65},
    {'name': '刘阿斗', 'chinese': 86, 'english': 83}
]
collection.insert_many(stu_list)

