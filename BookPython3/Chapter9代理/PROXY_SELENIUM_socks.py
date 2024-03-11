# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_SELENIUM_socks.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 11:08 
"""
from selenium import webdriver

proxy = '127.0.0.1:7891'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://' + proxy)
browser = webdriver.Chrome(options=options)
browser.get('https://www.httpbin.org/get')
print(browser.page_source)
browser.close()