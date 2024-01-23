# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PLAYWRIGHT_route.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/22 14:28 
"""
import re

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def cancel_request(route, request):
        route.abort()

    page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)  # 利用route实现网络劫持和修改
    page.goto("https://spa6.scrape.center")
    page.wait_for_load_state('networkidle')
    page.screenshot(path='image/no_picture.png')
    browser.close()

    # 将响应修改为自定义的html内容
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()

    def modify_response(route, request):
        route.fulfill(path='custom_response.html')

    # page.route('/', modify_response)          # 为什么没匹配到？
    page.route('**/*', modify_response)         # 修改了路由规则
    # '**/*' 匹配所有路径
    # ‘/'    匹配根路径
    # page.goto("https://spa6.scrape.center")
    page.goto("https://spa6.scrape.center/")

    browser.close()