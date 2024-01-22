# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：ASYNCIO_aiohttp.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/15 9:28 
"""

import asyncio
import aiohttp
import time
'''
只有使用支持异步操作的请求方式才可以实现真正的异步
aiohttp是一个支持异步请求的库
'''

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)