# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/13 21:40
@Auth ： 异世の阿银
@File ：run_spider1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from scrapy.cmdline import execute

execute("scrapy crawl quotes".split())
# execute(argv="scrapy crawl quotes".split(), settings=None)


'''
cmdline -> crawl -> crawler
'''