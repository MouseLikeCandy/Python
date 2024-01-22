# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 18:57
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
使用"."进行 xpath 连续调用, 实现连续搜索
'''
from scrapy.selector import Selector
html = '''
<html>
<body>
<bookstore>
<title>books</title>
<book>
<title>Novel</title>
<title lang="eng">Harry Potter</title>
<price>29.99</price>
</book>
<book>
<title>TextBook</title>
<title lang="eng">Learning XML</title>
<price>39.95</price>
</book>
</bookstore>
</body>
</html>
'''

selector = Selector(text=html)
selector.xpath('//title')
print(len(selector.xpath('//title')))       # 5

print(len(selector.xpath('//book/title')))  # 4

# 需求: 使用 xpath 语法第一次获取 selector 对象, 然后后续再次使用 selector 对象继续调用 xpath 语法,
# 也就是说, 在代码中可能会形成xpath的连环调用
selector1 = selector.xpath('//book')
# selector2 = selector1.xpath('/title')
selector2 = selector1.xpath('./title')   # 加一个点, 表示建立在上一个selector对象搜索的基础上继续搜索.
print(selector2)