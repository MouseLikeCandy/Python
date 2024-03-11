# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_PYPPETEER_http.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 14:26 
"""
import asyncio
from pyppeteer import launch

proxy = '127.0.0.1:7890'

async def main():
    browser = await launch({'args': ['--proxy-server=http://' + proxy], 'headless': False})
    page = await browser.newPage()
    await page.goto('https://www.httpbin.org/get')
    print(await page.content())
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())