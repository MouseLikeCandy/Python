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

# 1. 创建一个驱动对象
driver = webdriver.Chrome()     # 可以是别的浏览器: 火狐/IE

# 2. 发送请求
driver.get('http://127.0.0.1:5000')

# 3. 获取页面源代码
html = driver.page_source

# 4. 解析数据
user = driver.find_element(by=By.NAME, value='user')   # user 输入框
pwd = driver.find_element(by=By.NAME, value='pwd')   # pwd 输入框

# 输入内容
time.sleep(2)
user.send_keys('xxx')   # 发送关键字
time.sleep(2)
pwd.send_keys('123')
time.sleep(2)

# 关闭驱动
driver.close()
