# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_exception.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/18 13:24 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

'''
异常处理
'''

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element(By.ID, 'hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
