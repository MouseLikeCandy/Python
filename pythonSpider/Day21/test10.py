# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:46
@Auth ： 异世の阿银
@File ：test10.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath
使用 position()序号来确定所选择的元素    [position()=1]
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
print(selector.xpath('//book[position()=1]/title'))
# 简便写法
print(selector.xpath('//book[1]/title'))

# 最后一个
# print(selector.xpath('//book[-1]/title'))   # 错误的
print(selector.xpath('//book[position()=last()]/title'))
# 倒数第二个
print(selector.xpath('//book[position()=last()-1]/title'))