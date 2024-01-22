# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_multiWeb.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/18 9:59 
"""
import time
from selenium import webdriver

browser = webdriver.Chrome()
# 前进后退
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')
browser.back()
time.sleep(1)
browser.forward()

# 切换选项卡
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.python.org')

browser.close()