# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：ASYNCIO_coroutine.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/12 10:37 
"""
import asyncio

import requests


async def execute(x):
    print('Number: ', x)
    return x


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

task = asyncio.ensure_future(coroutine)     # 在声明loop之前先定义task
loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# task = loop.create_task(coroutine)
print('Task:', task)    # pending 挂起
loop.run_until_complete(task)
print('Task:', task)    # finished 完成 result=1
print('After calling loop')


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
