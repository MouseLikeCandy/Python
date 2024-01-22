# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 20:44
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
MongoDB
非关系型数据库
文档型数据库 类似JSON对象 类似Python中的字典类型
卓越的横向扩展能力  多种数据类型

SQL和noSQL的区别：
1. 在SQL中层次关系： 数据库 -> 表 -> 数据
2. 在noSQL中则是：  数据库 -> 集合 -> 文档

适合存储 文章， 评论
key 获取数据效率高

一般数据库会组合使用，没有通吃的数据库
'''

'''
pip install pymongo
'''
from pymongo import MongoClient     # 导入MongoDB的客户端


if __name__ == '__main__':
    # 1. 获取客户端连接对象
    uri = "mongodb://127.0.0.1:27017"    # 句柄（协议：//主机：端口号）
    client = MongoClient(uri)
    print(client)

    # 2. 操作 创建一个数据库
    db = client.student
    print(db)

    # 3. 创建数据表
    colletion = db.stu
    print(colletion)

