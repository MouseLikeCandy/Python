# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/15 20:28
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
scrapy 框架的执行流程图
1. REQUESTS      发送请求
7. ITEM/REQUESTS 封装数据模型/请求对象
8. ITEMS -> 进入管道    REQUESTS -> 进入调度器

Scrapy 框架的执行流程图: 1 / 7 / 8 这三个步骤是我们程序实现的.剩余的步骤都是 Scrapy 底层自动调度的.
'''
'''
quotes 网站 scrapy 提供的可供爬取的网站
http://quotes.toscrape.com/
http://quotes.toscrape.com/page/1/

项目位置 D:\Scrapy_example
'''