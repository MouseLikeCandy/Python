# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PYPPETEER_page.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/19 10:31 
"""
import asyncio
from pyppeteer import launch

weight, height = 1366, 768


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center')
    # 选择器方法
    await page.waitForSelector('.item .name')
    j_result1 = await page.J('.item .name')
    j_result2 = await page.querySelector('.item .name')
    jj_result1 = await page.JJ('.item .name')
    jj_result2 = await page.querySelectorAll('.item .name')
    print('J Result1:', j_result1)
    print('J Result2:', j_result2)
    print('JJ Result1:', jj_result1)
    print('JJ Result2:', jj_result2)
    # 选项卡操作
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    page = await browser.newPage()
    await page.goto('https://www.bing.com')
    pages = await browser.pages()
    print('Pages:', pages)
    page1 = pages[1]
    await page1.bringToFront()
    # 页面操作
    await page.goto('https://www.bing.com')    #'https://dynamic1.scrape.cuiqingcai.com/')
    await page.goto('https://spa2.scrape.center/')
    await page.goBack()     # 后退
    await page.goForward()  # 前进
    await page.reload()     # 刷新
    # await page.pdf({'path': 'pagePDF.pdf', 'format': 'A4'})        # 保存PDF, 需要无头模式
    await page.screenshot(path='image/pyppeteer_page.png')     # 截图
    await page.setContent('<h2>Hello World</h2>')   # 设置页面HTML
    await page.setUserAgent('Python')               # 设置User-Agent
    await page.setExtraHTTPHeaders(headers={})      # 设置headers
    await page.close()      # 关闭
    # 鼠标点击
    page = await browser.newPage()
    await page.bringToFront()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await page.click('.item .name', options={
        'button': 'right',
        'clickCount': 1,
        'delay': 3000
    })
    # 输入文本
    await page.goto('https://www.taobao.com')
    await page.type('#q', 'iPad')
    # 获取源代码和Cookies对象
    print('HTML:', await page.content())
    print('Cookies:', await page.cookies())
    await asyncio.sleep(10)
    # 执行JS
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio
        }
    }''')
    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
