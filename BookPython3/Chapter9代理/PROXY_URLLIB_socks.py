# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_URLLIB_socks.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/2/2 14:43 
"""
import socks
import socket
from urllib import request
from urllib.error import URLError


socks.setdefaultproxy(socks.SOCKS5, '127.0.0.1', 7891)
socket.socket = socks.socksocket
try:
    response = request.urlopen('https://www.httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)