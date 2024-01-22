# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PYPPETEER_launch.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/19 9:57 
"""
import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    browser = await launch(headless=False, devtools=True,   # 无头模式, 调试模式
                           userDataDir='./userdata',        # 用户目录Cache/Cookie等信息
                           args=['--disable-infobars',      # 禁用提示条
                                 f'--window-size={width},{height}'])     # 窗口大小
    # page = await browser.newPage()
    # 无痕模式
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    # 页面大小
    await page.setViewport({'width': width, 'height': height})
    # 绕过对WebDriver属性的检测
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: ()=>undefined})')
    # await page.goto('https://antispider1.scrape.center/')
    await page.goto('https://www.taobao.com/')
    await asyncio.sleep(100)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())