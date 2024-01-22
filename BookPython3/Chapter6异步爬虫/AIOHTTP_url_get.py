# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：AIOHTTP_url_get.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/15 10:17 
"""
import aiohttp
import asyncio
'''
get请求， 传递参数
'''


async def main():
    params = {'name': '郝小鱼', 'age': 20}
    timeout = aiohttp.ClientTimeout(total=1)    # 超时设置
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://www.httpbin.org/get', params=params) as response:
            print('status:', response.status)
            print('headers:', response.headers)
            print('body:', await response.text())
            print('bytes:', await response.read())
            print('json:', await response.json())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())