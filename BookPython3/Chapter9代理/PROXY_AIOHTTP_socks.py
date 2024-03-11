# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_AIOHTTP_socks.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 14:16 
"""
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector

connector = ProxyConnector.from_url('socks5://127.0.0.1:7891')


async def main():
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get('http://www.httpbin.org/get') as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())