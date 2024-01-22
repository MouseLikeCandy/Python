# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 19:28
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''

'''
import requests

# 简书
url = 'https://www.jianshu.com/'

# 通过改变'User-Agent'可以访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "X-Amzn-Trace-Id": "Root=1-6489988c-369241b710506fbe494991c2"
}
response = requests.get(url, headers=headers)
print(response.text)
print(type(response.headers))     # 大小写敏感的字典类型 <class 'requests.structures.CaseInsensitiveDict'>

# response 是requests 库定义的对象类型, 没有read()

print(response.headers['content-type'])