# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PYPPETEER_test02.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/19 9:02 
"""
import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    await page.screenshot(path='image/pyppeteer_test02.png')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }
    ''')

    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())