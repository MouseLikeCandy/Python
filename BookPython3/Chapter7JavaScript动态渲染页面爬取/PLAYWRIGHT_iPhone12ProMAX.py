# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PLAYWRIGHT_iPhone12ProMAX.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/22 13:39 
"""
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    print(p.devices.keys())
    iphone_12_pro_max = p.devices['iPhone 12 Pro Max']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_12_pro_max,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto('https://www.whatismybrowser.com/')
    page.wait_for_load_state(state='networkidle')       # 等待页面加载到指定状态
    # 其中state的默认值是load, 可选值：
    # domcontentloaded - 等到加载DOMContentLoaded事件
    # load - 等到加载load事件
    # networkidle - 网络空闲状态
    page.screenshot(path='image/browser-iphone.png')
    browser.close()