# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_REQUESTS_socks01.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:30 
"""
import requests

proxy = '127.0.0.1:7891'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('https://www.httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)