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
可以很容易的取出字典中的数据而不是从字符串中取数据

客户端(json字符串-> 字典) ---- HTTP协议 json数据 ---- 服务端(字典-> json字符串)

客户端: 将json格式的字符数据转换为字典来使用数据
'''
import json

# json 格式的字符串
json_str = '{"msg": "OK", "data": [{"stu_id": "1001", "name": "\u5f20\u4e09", "age": 18, "score": 88}, {"stu_id": "1002", "name": "\u674e\u56db", "age": 19, "score": 99}]}'


# 客户端
dict_data = json.loads(json_str)

print(type(json_str), json_str)  # json字符串转为字典类型

data = dict_data['data']
print(data)