# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_scrapeCenter.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/18 9:16 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
使用get_attribute方法获取节点的属性，但前提是得先选中这个节点
'''

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center/'
# 隐式等待
browser.implicitly_wait(10)
browser.get(url)
# 获取属性
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
print(logo)
print(logo.get_attribute('src'))
# 获取文本
title = browser.find_element(By.CLASS_NAME, 'logo-title')
print(title.text)
# 获取ID、位置、标签名和大小
print(title.id)
print(title.location)
print(title.tag_name)
print(title.size)