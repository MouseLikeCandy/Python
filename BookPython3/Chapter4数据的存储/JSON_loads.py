# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：JSON_loads.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/8 9:40 
"""
import json

str = """
[{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
"""
data = json.loads(str)
