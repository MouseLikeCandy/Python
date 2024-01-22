# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 20:11
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath 搜索元素的父节点
'''
from scrapy.selector import Selector
html = '''
<html>
<body>
<bookstore>
<book>
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
# /parent::* 表示当前标签的父标签对象
selector_list = selector.xpath('//title[@lang="chinese"]/parent::*')
for selector in selector_list:
    print(selector)