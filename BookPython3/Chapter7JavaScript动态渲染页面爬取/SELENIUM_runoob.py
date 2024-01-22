# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_runoob.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/17 16:04 
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# 切换到子Frame
browser.switch_to.frame('iframeResult')
# 动作链
source = browser.find_element(By.CSS_SELECTOR, '#draggable')
target = browser.find_element(By.CSS_SELECTOR, '#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
try:
    logo = browser.find_element(By.CLASS_NAME, 'logo')
except NoSuchElementException:
    print('NO LOGO')
# 切换回父Frame
browser.switch_to.parent_frame()
logo = browser.find_element(By.CLASS_NAME, 'logo')
print(logo)
print(logo.text)