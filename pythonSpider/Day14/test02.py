# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 18:28
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
Requests 基于urllib, 更加方便
pip install requests
'''


import requests


# urllib.request.urlopen()
# get请求
response = requests.get('http://www.baidu.com')
print(type(response))   # <class 'requests.models.Response'>    对象类型不一样, 操作方式不一样
print(dir(response))    # 看方法

# 文本数据          response.read().decode('uft-8')  HTTP对象
response.text    # requests.models.Response 对象

# 非文本数据     response.read()
response.content