# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/12 10:53
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
查询逻辑运算符
$lt: 存在并小于less than
$lte:存在并小于等于 less than and equal
$gt: 存在并大于 greater than
$gte: 存在并大于等于greater than and equal
$ne: 不存在或存在但不等于 not equal
$in:存在并在指定数组中
$nin:不存在或不在指定数组中 not in
$or: 匹配两个或多个条件中的一个
$and:匹配全部条件
'''
from pymongo import MongoClient
import pymongo

if __name__ == '__main__':
    # 1. 创建一个客户端
    client = MongoClient(host='localhost', port=27017)

    # 2. 获取数据库
    db = client.student

    # 3. 集合
    colletion = db.exam

    # 4. 对应的操作
    # 4.1 查询所有
    result_set = colletion.find()   # 参数中没有传递任何条件， 意味着查询所有
    for set in result_set:
        print(set)

    # 4.2 查询指定列的信息
    # find(参数1，参数2) 参数1： 查询条件  参数2： 指定的列名
    # _id列名默认显示
    result_set = colletion.find({}, {'name': 1, 'chinese': 1})  # find(参数1，参数2)
    result_set = colletion.find({}, {'_id': 0, 'name': 1, 'chinese': 1})
    for set in result_set:
        print(set)
    # 4.3 查询姓名为赵云的学生成绩, 英语成绩
    result_set = colletion.find({'name': '赵云'}, {'_id': 0, 'name': 1, 'english': 1})
    for set in result_set:
        print(set)
    # 4.4 查询英语成绩大于90的学生成绩
    result_set = colletion.find({'english': {'$gt': 90}})
    for set in result_set:
        print(set)
    # 4.5 查询英语成绩不等于70的学生成绩
    result_set = colletion.find({'english': {'$ne': 70}})
    for set in result_set:
        print(set)
    # 4.6 查询英语成绩在80-90之间的学生成绩
    result_set = colletion.find({'$and': [
        {'english': {'$gte': 80}},
         {'english': {'$lte': 90}}
    ]})
    for set in result_set:
        print(set)
    # 4.7 查询数学成绩为89,75,91的学生成绩
    result_set = colletion.find({'math': {'$in': [89, 75, 91]}})
    for set in result_set:
        print(set)
    # 4.8 插入一条数据, 刘阿斗没有数学成绩
    # 4.9 查询所有姓刘的学生成绩
    # regex 正则表达式
    result_set = colletion.find({'name': {'$regex': '^刘.*$'}})
    for set in result_set:
        print(set)
    # 4.10 查询数学成绩存在的学生成绩
    # exists
    result_set = colletion.find({'math': {'$exists': True}})
    for set in result_set:
        print(set)
    # 4.11 查询数学成绩不存在的学生成绩
    # exists
    result_set = colletion.find({'math': {'$exists': False}})
    for set in result_set:
        print(set)
    # 4.12 查询数学成绩大于80并且语文成绩大于80的学生成绩
    result_set = colletion.find({'$and': [
        {'math': {'$gt': 80}},
        {'chinese': {'$gt': 80}}
    ]})
    for set in result_set:
        print(set)
    # 4.13 查询数学成绩大于80或者语文成绩大于80的学生成绩
    result_set = colletion.find({'$or': [
        {'math': {'$gt': 80}},
        {'chinese': {'$gt': 80}}
    ]})
    for set in result_set:
        print(set)
    # 4.14 查询英语成绩不大于60分的学生成绩
    result_set = colletion.find({'english': {'$lte': 60}})
    for set in result_set:
        print(set)
    # 4.15 查询所有的语文成绩(不重复)
    result_set = colletion.find({}, {'_id': 0, 'chinese': 1}).distinct('chinese')
    for set in result_set:
        print(set)
    # 4.16 按语文成绩升序输出学生成绩
    result_set = colletion.find().sort('chinese', pymongo.ASCENDING)
    for set in result_set:
        print(set)
    # 4.17 按语文成绩升序输出学生成绩, 如果语文成绩相同, 按数学成绩降序排序
    result_set = colletion.find().sort([
        ('chinese', pymongo.ASCENDING),
        ('math', pymongo.DESCENDING)
    ])  # 如果第一个条件相同, 在根据第二个条件实现排序
    for set in result_set:
        print(set)

    # 5. 关闭资源
    client.close()