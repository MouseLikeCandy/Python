# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 19:38
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath 使用条件限定标签的属性 [@id = "b1"] [@language = "chinese"]
使用 condition 限定 tag 元素
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
湖南普门教育 湖南普门教育 湖南普门教育 湖南普门教育 湖南普门教育 湖南普门教育 湖南普门教育 湖南普门教育 湖南普门教育
<price>39.95</price>
</book>
</bookstore>
</body>
</html>
'''
selector = Selector(text=html)
# [] 表示添加标签的条件  如果标签需要添加属性条件, 千万不要忘记 @ 符号
# selector_list = selector.xpath('//book/title[@lang="chinese"]/text()')
# for selector in selector_list:
# print(selector.extract())
#
# print('-' * 100)
selector_list = selector.xpath('//book[@id="b2"]/title')
print(selector_list)
