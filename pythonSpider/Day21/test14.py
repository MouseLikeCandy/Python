# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 20:15
@Auth ： 异世の阿银
@File ：test14.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
xpath
搜索后面的兄弟节点, 指定标签后面的所有兄弟标签, 可以加条件限定
'''
from scrapy.selector import Selector
html = '''
<a>A1</a>
<b>B1</b>
<c>C1</c>
<d>D
    <e>E</e>
</d>
<b>B2</b>
<c>C2</c>
'''
selector = Selector(text=html)
selector_list = selector.xpath('//a/following-sibling::*')  # 指定标签后面的所有兄弟标签
print(selector_list.extract())

selector_list = selector.xpath('//a/following-sibling::*[position()=1]')
print(selector_list.extract())

selector_list = selector.xpath('//b[position()=2]/following-sibling::*')
print(selector_list.extract())