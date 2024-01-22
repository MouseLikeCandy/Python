# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/9 6:40
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
JSON转换测试
'''
import json

# json 格式的字符串
json_str = '{"msg": "OK", "data": [{"stu_id": "1001", "name": "\u5f20\u4e09", "age": 18, "score": 88}, {"stu_id": "1002", "name": "\u674e\u56db", "age": 19, "score": 99}]}'

print(type(json_str), json_str)

data = json_str['data']
print(data)