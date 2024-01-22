# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 20:06
@Auth ： 异世の阿银
@File ：test12.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath
使用@*代表任何属, 星号表示通配符, 通配属性
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
selector_list = selector.xpath('//book[@*]/title')      # book 必须要有属性
# selector_list = selector.xpath('//book/title')
for selector in selector_list:
    print(selector)