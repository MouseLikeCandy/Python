# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SELENIUM_anti.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/18 13:45 
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions

'''
反屏蔽 anti-shielding
网站增加了对Selenium的检测，检测浏览器窗口下的window.navigator对象中是否包含webdriver
'''

option = ChromeOptions()
option.add_argument('--headless')   # 无头模式，不弹窗口
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)     # 自动化扩展


# 反Selenium屏蔽
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {  # CDP方法
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
browser.get('https://antispider1.scrape.center')

# 设置窗口大小-加载-截图
browser.set_window_size(1920, 1080)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('image/preview.png')