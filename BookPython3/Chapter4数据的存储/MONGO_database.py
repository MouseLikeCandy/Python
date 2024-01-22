# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：MONGO_database.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/9 9:06 
"""
import pymongo

# 连接MongoDB
# 创建MongoDB的连接对象
# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')
print(client)

# 指定数据库
# db = client.test
db = client['test']

# 指定集合
# collection = db.students
collection = db['students']

# 插入数据-单条
student = {
    'id': '20240109',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)
print(result)
print(result.inserted_id)

# 插入数据-多条
student1 = {
    'id': '20240109001',
    'name': '高振峰',
    'age': 22,
    'gender': 'male'
}

student2 = {
    'id': '20240109002',
    'name': '袁悦',
    'age': 20,
    'gender': 'female'
}

student3 = {
    'id': '20240109003',
    'name': '张志勇',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2, student3])
print(result)
print(result.inserted_ids)

# 查询
result = collection.find_one({'name': '张志勇'})
print(type(result))
print(result)

# 根据ObjectId来查询
from bson.objectid import ObjectId

result = collection.find_one({'_id': ObjectId('659c9ff03d4aeeadc8c77b21')})
print(result)

# results = collection.find({'gender': 'male'})
# results = collection.find({'age': {'$gt': 20}})
results = collection.find({'name': {'$regex': '^高.*'}})
print(results)
for result in results:
    print(result)

# 统计数据条数
count = collection.count_documents({})
print(count)
query = {'name': {'$regex': '^高.*'}}
count = collection.count_documents(query)
print(count)

# 排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(50)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(50).limit(2)
print([result['name'] for result in results])

# 更新
condition = {'name': '高振峰'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

results = collection.update_many(condition, {'$inc': {'age': 1}})
print(results)
print(results.matched_count, results.modified_count)

# 删除
result = collection.delete_one({'name': '张志勇'})
print(result)
print(result.deleted_count)

result = collection.delete_many({'age': {'$lt': 21}})
print(result.deleted_count)

