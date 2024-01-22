# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:52
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath
使用*代表任何 element 元素, 星号表示通配符, 通配标签
'''
from scrapy.selector import Selector
html = '''
<html>
<body>
<bookstore>
<book id='b1'>
<title lang="english">Harry Potter</title>
<price>29.99</price>
</book>
<div id='b2'>
<title lang="chinese">学习 XML</title>
<price>39.95</price>
</div>
</bookstore>
</body>
</html>
'''
selector = Selector(text=html)
# print(selector.xpath('//bookstore/title'))  # title 不是bookstore的子标签/两个名字不一样
selector_list = selector.xpath('//bookstore/*/title')
for selector in selector_list:
    print(selector)