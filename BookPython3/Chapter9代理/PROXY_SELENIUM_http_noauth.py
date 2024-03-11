# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_SELENIUM_http_noauth.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:56 
"""
from selenium import webdriver

proxy = '127.0.0.1:7890'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(options=options)
browser.get('https://www.httpbin.org/get')
print(browser.page_source)
browser.close()