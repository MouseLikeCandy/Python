# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_HTTPX_http.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:39 
"""
import httpx

proxy = '127.0.0.1:7890'
proxies = {
    'http://': 'http://' + proxy,
    'https://': 'https://' + proxy,
}

with httpx.Client(proxies=proxies) as client:
    response = client.get('https://www.httpbin.org/get')
    print(response.text)
