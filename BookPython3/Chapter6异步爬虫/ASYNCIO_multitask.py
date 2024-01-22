# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：ASYNCIO_multitask.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/12 11:04 
"""
import asyncio
import requests


async def request():
    # url = 'http://www.baidu.com'
    url = 'https://www.httpbin.org/delay/5'     # 体现携程的优势
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Task:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
