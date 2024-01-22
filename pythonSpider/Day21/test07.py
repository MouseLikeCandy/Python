# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:33
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath 获取文本数据, 获取节点的文本值
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
<book id='b2'>
<title lang="chinese">学习 XML</title>
<price>39.95</price>
</book>
</bookstore>
</body>
</html>
'''
selector = Selector(text=html)
selector_list = selector.xpath('//book/title/text()')   # /text() 获取 title 标签中的文本数据
for selector in selector_list:
    print(selector.extract())