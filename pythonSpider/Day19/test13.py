# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/12 10:04
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from pymongo import MongoClient

if __name__ == '__main__':
    # 1. 获取客户端对象
    client = MongoClient(host='localhost', port=27017)
    print(client)

    # 2. 创建数据库
    db = client['student']
    print(db)

    # 3. 获取集合对象
    collection = db['stu']
    print(collection)

    # 4. 查询数据
    doc = collection.find_one({'stu_id': '1002'})
    print(doc)  # 文档数据类型，是 json document, 类似于 Python 中的字典数据类型

    result_set = collection.find()
    for row in result_set:
        print(row)

    # 5. 关闭资源
    client.close()