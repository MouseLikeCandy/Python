# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:21
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath
获取元素属性值
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
# 需求: 希望获取 book 标签中 id 对应的属性值
slector_list = selector.xpath('//book/@id')        # /@id 当前标签中的 id 属性值
for selector in slector_list:
    print(selector.extract())
    # print(selector.get())
    # print(selector.getall())    # 返回的是一个列表
    # print(selector.extract_first())   # 主要是给列表[selector1, selector2, selector3, ...]使用的, 需要selector是一个列表


'''
总结: 循环中取数据, 就直接使用 extract(), 可以不考虑别的方法.
'''