# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：AIOHTTP_asyncio.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/15 9:50 
"""
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'http://cuiqingcai.com')
        print(f'html: {html[:100]}...')


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()   # 启用事件循环
    # loop.run_until_complete(main())   # 运行
    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())     # 3.7及以后得启动操作，run方法内部自动启动一个事件循环

