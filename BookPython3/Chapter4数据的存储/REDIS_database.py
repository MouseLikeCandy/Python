# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：REDIS_database.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/9 10:40 
"""
from redis import StrictRedis

# 连接方式一
redis = StrictRedis(host='localhost', port=6379, db=0, password='123456')
redis.set('name', '张志勇')
print(redis.get('name').decode('utf-8'))
redis.close()

from redis import ConnectionPool

# 连接方式二
pool = ConnectionPool(host='localhost', port=6379, db=0, password='123456')
redis = StrictRedis(connection_pool=pool)
print(redis.get('name').decode('utf-8'))
redis.close()

# # 连接方式三
url = 'redis://:123456@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
print(redis.get('name').decode('utf-8'))
redis.close()

