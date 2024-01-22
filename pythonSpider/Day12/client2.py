# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/24 20:19
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
from bs4 import BeautifulSoup

'''
BeautifulSoup解析库拥有一定的容错能力
test2.html
'''
url = 'http://127.0.0.1:5000'

# 发送请求, 获取响应
response = urllib.request.urlopen(url)
# 读取数据, html就是网页源代码, 不是解析后的数据
html = response.read().decode()

# 使用BeautifulSoup解析库将html字符串类型转换为'文档树'类型的数据对象
# BeautifulSoup解析库拥有一定的容错能力
soup = BeautifulSoup(html, 'html.parser')
print(type(soup), soup)



