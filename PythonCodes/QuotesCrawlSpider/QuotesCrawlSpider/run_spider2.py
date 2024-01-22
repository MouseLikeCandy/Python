# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/13 21:40
@Auth ： 异世の阿银
@File ：run_spider1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
通过看源码可以找到更底层的运行方法

(CrawlerProcess(CrawlerRunner))(Crawler最底层)
'''

from scrapy.crawler import CrawlerProcess
from QuotesCrawlSpider.QuotesCrawlSpider.spiders import quotes
from QuotesCrawlSpider.QuotesCrawlSpider.spiders.quotes import QuotesSpider as QuotesSpider1
from QuotesCrawlSpider.QuotesCrawlSpider.spiders.quotes2 import QuotesSpider as QuotesSpider2

crawler_process = CrawlerProcess()
# crawler_process = CrawlerProcess(settings=None)
# crawler_process = CrawlerProcess(settings={})

# crawler_process.crawl("quotes", )   # KeyError: 'Spider not found: quotes'   参数类型需要: crawler_or_spidercls 爬虫类
# crawler_process.crawl(quotes)   # AttributeError:
# module 'QuotesCrawlSpider.QuotesCrawlSpider.spiders.quotes' has no attribute 'update_settings'

# 一个进程里面跑两个爬虫
crawler_process.crawl(QuotesSpider1)     # 初始化scrapy的加载项
crawler_process.crawl(QuotesSpider2)     # 初始化scrapy的加载项
# 以下可以有多个爬虫


crawler_process.start(stop_after_crawl=True)     # 真正的启动爬虫 # stop_after_crawl=False跑完程序不停, 执行其他的东西twisted



# 两个爬虫一起跑, 哪个先跑完不一定