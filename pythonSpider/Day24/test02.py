# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 19:55
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time

'''
使用 selenium 自动输入用户名和密码, 然后 自动点击 登录按钮

'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 登录操作
def login():
    # 4. 解析数据
    user = driver.find_element(by=By.NAME, value='user')   # user 输入框
    pwd = driver.find_element(by=By.NAME, value='pwd')   # pwd 输入框
    login = driver.find_element(by=By.NAME, value='login')

    # 向输入框中输入内容
    # time.sleep(2)
    user.send_keys('xxx')   # 发送关键字
    # time.sleep(2)
    pwd.send_keys('123')
    # time.sleep(2)

    # 登录按钮实现点击操作
    login.click()

# 爬虫爬取
def spider_crawl():
    # 获取页面所有的tr标签
    trs = driver.find_elements(by=By.TAG_NAME, value='tr')
    # print(len(trs))
    for i in range(1, 4):
        tds = trs[i].find_elements(by=By.TAG_NAME, value='td')
        # 遍历 tds / 使用下标从列表中直接取出元素
        if len(tds) == 3:
            mark = tds[0].text
            model = tds[1].text
            price = tds[2].text
            print(mark, model, price)

if __name__ == '__main__':
    # 1. 创建一个驱动对象
    driver = webdriver.Chrome()  # 可以是别的浏览器: 火狐/IE

    # 2. 发送请求
    driver.get('http://127.0.0.1:5000')

    # 3. 获取页面源代码
    html = driver.page_source

    # 调用登录
    login()

    # 爬取数据
    spider_crawl()

    # 5. 关闭驱动
    driver.close()
