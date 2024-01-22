# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：ASYNCIO_callback.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/12 10:58 
"""
import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

def callback(task):
    print('Status:', task.result())

coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('Task:', task.result())