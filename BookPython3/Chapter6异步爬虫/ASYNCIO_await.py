# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：ASYNCIO_await.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/15 8:57 
"""
import asyncio
import requests
import time

'''
要实现异步处理，先得有挂起操作
'''
start = time.time()


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    # response = requests.get(url)
    response = await requests.get(url)  # 将耗时等待的操作挂起
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:'. end - start)