# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 18:00
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
Selenium 框架
解决scrapy处理不了的问题, url.request.open 也解决不了的问题

异步发送请求的问题

网页数据是活的, 不是死的; 数据根据鼠标的滚动自动发送请求, 一开始没有数据, 后来有数据了
右键检查 XHR  XMLHttpRequest 异步请求对象, 会看到新的请求的发送, 不是主动发的

Selenium是一个模拟浏览器执行请求行为的一个框架

1. 安装 pip install selenium
2. 下载谷歌驱动程序 http://chromedriver.storage.googleapis.com/index.html  116.0.5845.97  
    将 chromedriver.exe 放到解释器目录下(File -- Setting -- Python Interpreter)
    chromedriver.exe 是用来操作系统上的浏览器的
3. selenium官方文档 https://selenium-python-zh.readthedocs.io/en/latest/
'''