# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_zhihu.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/18 9:08 
"""
from selenium import webdriver
import time
'''
对于selenium没有提供API的操作，可以模拟运行JavaScript
'''

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

# cookie操作
print(browser.get_cookies())
browser.add_cookie({'name': '王小鱼', 'domain': 'www.zhihu.com', 'value': '1234567890'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
# 模拟运行JavaScript
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
time.sleep(2)

