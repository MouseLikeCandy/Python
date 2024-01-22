# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/24 20:19
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
# import bs4    # 导入方式
from bs4 import BeautifulSoup
url = 'http://127.0.0.1:5000'

# 发送请求, 获取响应
response = urllib.request.urlopen(url)
# 读取数据, html就是网页源代码, 不是解析后的数据
html = response.read().decode()

print(type(html), html)       # <class 'str'>

# 需求: 取出三个超链接


# 说明: 不同的数据类型,就有不同的操作行为
# 说明: 网页源代码是str类型, 获取数据就会非常复杂和麻烦. 用正则直接处理该字符串非常不合理.
# 文档树类型  document类型 - > html节点 - > head -> meta
#                                             -> title
#                                    - > body -> p          属性class='story'     数据Once upon a time
#                                             -> p -> a     属性href="http://example.com/elsie"   数据Elsie
#                                                  -> a
#                                                  -> a
#                                             -> p

# str类型 -> 通过BeautifulSoup解析 -> document文档树结构类型

print('-' * 100)
# soup = bs4.BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, 'html.parser')
print(type(soup), soup)  # <class 'bs4.BeautifulSoup'>
# 类型变了, 操作方式不一样
# 说明: 不同的数据类型, 就拥有不同的操作行为.



