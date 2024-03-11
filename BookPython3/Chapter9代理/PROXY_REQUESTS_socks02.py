# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_REQUESTS_socks02.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:35 
"""
import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7891)
socket.socket = socks.socksocket

try:
    response = requests.get('https://www.httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)