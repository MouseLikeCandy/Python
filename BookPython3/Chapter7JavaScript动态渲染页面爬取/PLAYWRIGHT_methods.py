# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PLAYWRIGHT_methods.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/22 13:59 
"""
from playwright.sync_api import  sync_playwright


def on_response(response):
    # print(f'Status {response.status}: {response.url}')  # 输出结果对应浏览器的network中的内容
    if '/api/movie/' in response.url and response.status == 200:
        print(response.json())


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.on('response', on_response)    # on方法监听response事件，关联回调函数
    page.goto('https://spa6.scrape.center')
    page.wait_for_load_state('networkidle')
    print('页面源代码：', page.content())
    href = page.get_attribute('a.name', 'href')
    print('获取节点属性', href)
    elements = page.query_selector_all('a.name')    # 获取所有节点
    for element in elements:
        print(element.get_attribute('href'))
        print(element.text_content())
    element = page.query_selector('a.name')
    print(element.get_attribute('href'))
    print(element.text_content())
    browser.close()