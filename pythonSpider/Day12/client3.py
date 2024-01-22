# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/24 20:19
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
# import bs4
from bs4 import BeautifulSoup
url = 'http://127.0.0.1:5000'

# 发送请求, 获取响应
response = urllib.request.urlopen(url)
# 读取数据, html就是网页源代码, 不是解析后的数据
html = response.read().decode()

print(type(html), html)       # <class 'str'>

# 需求: 取出三个超链接

print('-' * 100)
# soup = bs4.BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, 'html.parser')
print(type(soup), soup)         # <class 'bs4.BeautifulSoup'>

# 需求: 查找文档中的<title>元素
tag = soup.find('title')
# tag是标签类型的对象, 后期我们通过对应的行为操作该对象
print(type(tag), tag)   # <class 'bs4.element.Tag'>

# 需求: 查找文档中所有的<a>元素
tags = soup.find_all('a')
# find()只返回找到的第一个符合的标签
print(type(tags), tags)  # <class 'bs4.element.ResultSet'> 结果集类型, 类似Python的列表类型

for tag in tags:
    # 遍历ResultSet后取出的每一个都是<class 'bs4.element.Tag'>类型
    print(type(tag), tag)

# 需求: 查找class='title'的<p>标签
# 添加属性条件的方式
tags = soup.find_all('p', attrs={'class': 'title'})       # attributes属性
for tag in tags:
    print(tag)

# 需求: 查找文档中class='sister'的元素
# name=None表示没有指定标签, 所有标签都可以, 但是后面有一个属性条件
tags = soup.find_all(name=None, attrs={'class': 'sister'})
# tags = soup.find_all(attrs={'class': 'sister'})
for tag in tags:
    print(tag)



