# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 20:53
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 通过 selenium 获取Ajax请求数据
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 爬虫函数
def spider():
    # tr 标签
    trs = driver.find_elements(by=By.TAG_NAME, value='tr')
    for i in range(1, len(trs)):
        tds = trs[i].find_elements(by=By.TAG_NAME, value='td')
        if len(tds) == 2:
            model = tds[0].text
            price = tds[1].text
            print(f'{model} - {price}')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5000')
    html = driver.page_source
    select = driver.find_element(by=By.ID, value='marks')
    options = select.find_elements(by=By.TAG_NAME, value='option')
    # 遍历 options 列表
    for option in options:
        # 点击选择框对象
        option.click()
        # 爬取数据
        spider()
        # 停留
        time.sleep(2)

    driver.close()