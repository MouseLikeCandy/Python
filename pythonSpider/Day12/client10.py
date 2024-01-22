# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/24 21:09
@Auth ： 异世の阿银
@File ：client7.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
from bs4 import BeautifulSoup
'''
之前用 find find_all 
现在用 css选择器  写法select
test3.html
'''
response = urllib.request.urlopen('http://127.0.0.1:5000')
html = response.read().decode()
# 将页面转换为文档树类型
soup = BeautifulSoup(html, 'html.parser')
# select()方法中可以书写css语法
tag = soup.select('#position_table')    # css 指定id
print(tag)

tag = soup.select('.even')  # css 指定class
print(tag)

# CSS返回的是一个列表, 哪怕只有一个元素

tag = soup.select('td[class = 1 square]')   # css 指定条件选择器  条件class = 1 square的td元素
# = 指定属性值
# ^= 以什么开头
# $= 以什么结尾
# *= 包含指定的每个元素
print(tag)


tag = soup.select('p a')    # CSS语法中的'空格'表示子孙标签
print(tag)
tag = soup.select('p>a')    # CSS语法中的'>'表示直接子标签
print(tag)


# select 查找子孙节点
# 简单的文本测试
# 两个案例:
# 爬取天气预报    http://www.weather.com.cn 取出7天数据放到数据库中, 定位到数据  北上广深
# 取出数据放到数据库中
# 中国大学排名    https://shanghairanking.cn/rankings/bcur/2023
