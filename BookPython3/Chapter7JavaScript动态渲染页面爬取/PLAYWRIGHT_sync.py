# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PLAYWRIGHT_sync.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/19 15:07 
"""
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    for browser_type in [p.chromium, p.webkit]:     # , p.firefox会卡
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'image/sync-screenshot-{browser_type.name}.png')
        print(page.title())
        browser.close()
