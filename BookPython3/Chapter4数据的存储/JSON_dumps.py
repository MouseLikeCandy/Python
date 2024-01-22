# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：JSON_dumps.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/8 9:36 
"""
import json

data = [{
    'name': '王小鱼',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

with open('data_dumps.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))