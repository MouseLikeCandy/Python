# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_taobao.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/17 15:17 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化浏览器对象
browser = webdriver.Chrome()
# 加载页面
browser.get('https://www.taobao.com')
# print(browser.page_source)
# 显示等待, 等待条件
wait = WebDriverWait(browser, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(search_box, button)
# 查找节点
# input_first = browser.find_element(by=By.NAME, value='q')
input_first = browser.find_element(By.ID, 'q')
input_second = browser.find_element(by=By.CSS_SELECTOR, value='#q')
input_third = browser.find_element(by=By.XPATH, value='//*[@id="q"]')
print(input_first, input_second, input_third)
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
# 节点交互
input_first.send_keys('iPhone')
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')
button = browser.find_element(By.CLASS_NAME, 'btn-search')
button.click()
browser.close()