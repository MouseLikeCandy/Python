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

'''
注意点: 浏览器发送请求延时的现象
出现延时怎么办? 可能拿不到数据

自己实现强制等待, 循环等待
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')
html = driver.page_source


# 强制等待
# time.sleep(1.5)     # 合理吗? 不合理, 时间不确定
# driver.implicitly_wait(1.5)     # selenium隐式等待

# 循环等待(自己实现)
wait_time = 0
options = []

while wait_time <= 10:
    # 尝试获取获取 select 标签中的 option 标签
    options = driver.find_elements(by=By.XPATH, value='//select/option')
    if len(options) > 0:
        # 拿到数据, 结束循环
        break

    time.sleep(0.5)
    wait_time += 0.5

# 判断是否超时
if wait_time >= 10:
    # 手动抛出异常, 不做try catch 终止
    raise Exception('waiting time out!')

# 遍历 options 列表
for option in options:
    print(option.text)


# # 获取 select 标签中的 option 标签
# options = driver.find_elements(by=By.XPATH, value='//select/option')
# print(len(options))


driver.close()