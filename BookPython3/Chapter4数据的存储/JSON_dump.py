# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：JSON_dump.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/8 9:49 
"""
import json

data = [{
    'name': '王小鱼',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

json.dump(data, open('data_dump.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)