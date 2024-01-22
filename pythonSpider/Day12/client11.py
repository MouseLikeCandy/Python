# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/12 17:59
@Auth ： 异世の阿银
@File ：client11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
使用CSS语言实现子孙节点查找
select 
'''
from bs4 import BeautifulSoup

# 模拟页面数据
doc = '''
<div>
<p>A</p>
<span><p>B</p></span>
</div>
<div>
<p>C</p>
</div>
'''

# 将页面转为文档树类型
soup = BeautifulSoup(doc, 'html.parser')
# select() 方法中可以书写 CSS 语法
# 空格 子孙节点
# > 子节点
tags = soup.select('div p')    # 查找div标签内部所有p子孙标签
for tag in tags:
    print(tag)

tags = soup.select('div > p')    # 查找div标签内部所有p子标签
for tag in tags:
    print(tag)

