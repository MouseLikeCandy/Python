# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 20:53
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 通过 selenium 获取Ajax请求数据 / 学习JS 分析请求
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')
html = driver.page_source
print(html)
driver.close()