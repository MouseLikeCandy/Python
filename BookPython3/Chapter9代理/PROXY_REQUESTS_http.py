# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_REQUESTS_http.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/6 10:23 
"""
import requests

proxy = 'username:password@127.0.0.1:7890'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}
try:
    response = requests.get('https://www.httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)