# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_HTTPX_socks_async.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:49 
"""
import httpx
import asyncio
from httpx_socks import AsyncProxyTransport

transport = AsyncProxyTransport.from_url('socks5://127.0.0.1:7891')

async def main():
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get('https://www.httpbin.org/get')
        print(response.text)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())