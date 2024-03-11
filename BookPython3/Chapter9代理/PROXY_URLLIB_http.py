# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_URLLIB_http.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/2/2 10:12 
"""
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


proxy = 'user-001:123456@127.0.0.1:7890'    # 在自己的计算机上启动HTTP代理服务
# proxy = 'username:password@127.0.0.1:7890'    # 带用户名密码
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
    # 'ftp': 'ftp://' + proxy
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
