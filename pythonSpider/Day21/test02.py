# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 18:33
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
scrapy 中查找HTML 元素
XPath
'''
from scrapy.selector import Selector


html = '''
<html>
<body>
<bookstore>
<book>
<title lang="eng">Harry Potter</title>
<price>29.99</price>
</book>
<book>
<title lang="eng">Learning XML</title>
<price>39.95</price>
</book>
</bookstore>
</body>
</html>
'''

# 创建一个选择器对象
selector = Selector(text=html)
# selector.xpath()    # 后期可以直接使用response.xpath
print(selector)     # <Selector xpath=None data='<html>\n<body>\n<bookstore>\n<book>\n<tit...'>
print(type(selector))

# 需求: 查找真个数据中的所有的 title 标签
# xpath('//title'): 全文档搜索 title 标签
titles = selector.xpath('//title')
for title in titles:
    # title 依然是 Selector 对象, 但里面的数据是title数据
    print(title)


