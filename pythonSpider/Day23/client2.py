# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 18:52
@Auth ： 异世の阿银
@File ：client2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium.webdriver.chrome.options import Options

'''
用selenium实现客户端
'''
from selenium import webdriver  # 网页驱动
import time

chrome_options = Options()
chrome_options.add_argument('--headless')       # 不显示浏览器
chrome_options.add_argument('--disable-gpu')    # 禁用gpu 图形界面gpu

# 创建一个 chrome 浏览器 驱动对象
driver = webdriver.Chrome(options=chrome_options)
# 发送请求
driver.get('http://127.0.0.1:5000')
# 获取页面数据
html = driver.page_source   # 说明: 通过selenium框架获取到的数据一定是与浏览器中看到的数据是一模一样的.
print(html)

# time.sleep(2)       # 显示浏览器2秒

# 关闭浏览器
driver.close()