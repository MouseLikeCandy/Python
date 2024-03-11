# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_AIOHTTP_http.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 14:12 
"""
import asyncio
import aiohttp

proxy = 'http://127.0.0.1:7890'

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.httpbin.org/get', proxy=proxy) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())