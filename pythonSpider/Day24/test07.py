# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/20 12:10
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
注意点: 浏览器发送请求延时的现象
出现延时怎么办? 可能拿不到数据

selenium 实现循环等待
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')
html = driver.page_source

# 循环等待(selenium实现)
# WebDriverWait 浏览器驱动等待对象
# until 直到..才
# expected_conditions   期待条件
# presence_of_element_located 定位元素的出现
# 元素对象是一个元组的数据类型(By.XPATH, '//select/option') 注意: 这个元组中不能写关键字名称
WebDriverWait(driver=driver, timeout=10, poll_frequency=0.5).until(
    expected_conditions.presence_of_element_located((By.XPATH, '//select/option')))     # 元组()


# 获取 select 标签中的 option 标签
options = driver.find_elements(by=By.XPATH, value='//select/option')
for option in options:
    print(option.text)


driver.close()