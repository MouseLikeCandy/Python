# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_baidu.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/17 14:32 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.Safari()

try:
    browser.get('https://www.baidu.com')
    input = browser.find_element(by=By.ID, value='kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


