# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_HTTPX_socks_sync.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:47 
"""
import httpx
from httpx_socks import SyncProxyTransport

transport = SyncProxyTransport.from_url('socks5://127.0.0.1:7891')

with httpx.Client(transport=transport) as client:
    response = client.get('https://www.httpbin.org/get')
    print(response.text)