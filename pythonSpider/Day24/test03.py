# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 20:20
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 普通请求无法获取Ajax请求数据
import urllib.request

response = urllib.request.urlopen('http://127.0.0.1:5000/')
html = response.read().decode()
print(html)     # select 标签下没有数据, 可以对比查看浏览器

