# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/9 6:46
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
服务端: 将数据转换为json格式的字符串返回给客户端
'''

import json

# 服务端
data_dict = {"msg": "OK", "data": [{"stu_id": "1001", "name": "张三", "age": 18, "score": 88}, {"stu_id": "1002", "name": "李四", "age": 19, "score": 99}]}

print(type(data_dict), data_dict)

json_str = json.dumps(data_dict)    # 字典类型转为json字符串

print(type(json_str), json_str)
