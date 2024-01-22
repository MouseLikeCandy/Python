# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 18:46
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from scrapy.selector import Selector
'''
xpath
'//' 和 '/'
'''

html = '''
<html>
<body>
<bookstore>
<book>
<title lang="eng">Harry Potter</title>
<price>29.99</price>
</book>
<book>
<title lang="eng">Learning XML</title>
<price>39.95</price>
</book>
</bookstore>
</body>
</html>
'''

# 1. 创建一个 selector 选择器对象
selector = Selector(text=html)

# 2. 调用对象的 xpath 语法实现数据的搜索
# xpath('//bookstore/book') 全文档搜索 bookstore 标签, 然后在 bookstore 标签下搜索 book 直接子标签
books = selector.xpath('//bookstore/book')
for book in books:
    print(book)

print('-' * 100)

books = selector.xpath('//body/book')   # 只能搜索到直接子标签
for book in books:
    print(book)

print('-' * 100)

books = selector.xpath('//body/bookstore/book')
for book in books:
    print(book)

print('-' * 100)

# xpath('//body//book') 第二个book 标签全文档搜索是建立在第一个搜索结果上实现的.
books = selector.xpath('//body//book')
for book in books:
    print(book)

print('-' * 100)