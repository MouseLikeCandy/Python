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

    # 4. 删除数据
    # collection.delete_one({'name': '张三'})
    collection.delete_one({'gender': '男'})  # 如果有多条数据满足条件，也只删除第一条满足的数据
    collection.delete_many({'score': 88.5})

    # 5. 关闭资源
    client.close()