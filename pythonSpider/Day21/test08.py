# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:35
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath
获取文本数据, 获取多个文本节点值
'''
from scrapy.selector import Selector
html = '''
<html>
<body>
<bookstore>
<book id='b1'>
<title lang="english"><b>H</b>arry <b>P</b>otter</title>
<price>29.99</price>
</book>
</bookstore>
</body>
</html>
'''
selector = Selector(text=html)
selector_list = selector.xpath('//book/title/text()')   # /text() 获取 title 标签中的文本数据, 不会取<b>标签中的数据
for selector in selector_list:
    print(selector.extract())