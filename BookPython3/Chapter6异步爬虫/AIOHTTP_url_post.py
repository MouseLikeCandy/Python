# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：AIOHTTP_url_post.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/15 10:49 
"""
import asyncio
import aiohttp
'''
post请求
如果返回的是一个协程对象(如async 修饰的方法)，那么前面就需要await，具体看aiohttp的API
https://docs.aiohttp.org/en/stable/client_reference.html
'''


async def main():
    data = {'name': '郝小鱼', 'age': 20}
    timeout = aiohttp.ClientTimeout(total=1)  # 超时设置
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # async with session.post('https://www.httpbin.org/post', data=data) as response:
        async with session.post('https://www.httpbin.org/post', json=data) as response:
            print('status:', response.status)
            print('headers:', response.headers)
            print('body:', await response.text())
            print('bytes:', await response.read())
            print('json:', await response.json())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())