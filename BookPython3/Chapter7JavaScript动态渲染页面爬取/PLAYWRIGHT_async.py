# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PLAYWRIGHT_async.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/19 15:42 
"""
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'image/async-screenshot-{browser_type.name}.png')
            print(await page.title())
            await browser.close()

asyncio.run(main())