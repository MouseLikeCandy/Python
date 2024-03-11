# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_PLAYWRIGHT_http.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 14:32 
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(proxy={
        'server': 'http://127.0.0.1:7890'
    })
    page = browser.new_page()
    page.goto('https://www.httpbin.org/get')
    print(page.content())
    browser.close()