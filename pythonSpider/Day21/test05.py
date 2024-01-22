# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:06
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
 extract 与 extract_first 函数使用, 抽取数据
'''
from scrapy.selector import Selector
html = '''
<html>
<body>
<bookstore>
<title>books</title>
<book id='b1'>
<title lang="english">Harry Potter</title>
<price>29.99</price>
</book>
<book id='b2'>
<title lang="chinese">学习 XML</title>
<price>39.95</price>
</book>
</bookstore>
</body>
</html>
'''

selector = Selector(text=html)
prices = selector.xpath('//book/price')
print(prices)
# [<Selector xpath='//book/price' data='<price>29.99</price>'>,
# <Selector xpath='//book/price' data='<price>39.95</price>'>]

# 需求: 获取 selector 对象中的 data 数据
for price in prices:
    # data = price.extract()      # extract 抽取数据, 获取的就是 selector 对象中对应的data数据
    data = price.get()
    print(data)

print('-' * 100)

datas = selector.xpath('//book/price').extract()    # extract() 返回的是一个列表, 列表中不是selector对象, 而是标签对象.
print(datas)

print('-' * 100)

datas = selector.xpath('//book/price').getall()    # getall() 等价于 extract()
print(datas)

print('-' * 100)

# datas = selector.xpath('//book/price').get()     # get() 返回的是一个标签对象.
datas = selector.xpath('//book/price').extract_first()    # extract_first() 等价于 get()
print(datas)

