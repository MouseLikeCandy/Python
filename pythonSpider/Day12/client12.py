# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/12 18:24
@Auth ： 异世の阿银
@File ：client12.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
使用CSS语言实现兄弟节点查找
select 
'''
from bs4 import BeautifulSoup

# 模拟页面数据
doc = '''
<body>
demo
<div>A</div>
<b>X</b>
<p>B</p>
<span>
<p>C</p>
</span>
<p>D</p>
</body>
'''


# 将页面转为文档树类型
soup = BeautifulSoup(doc, 'html.parser')
# select() 方法中可以书写 CSS 语法
# 空格 子孙节点
# > 子节点
# ~ 兄弟节点
tags = soup.select('div ~ p')    # 查找div标签同级的所有兄弟p标签
for tag in tags:
    print(tag)

tags = soup.select('div + p')    # 查找div标签同级的第一个兄弟p标签   挨着的
for tag in tags:
    print(tag)