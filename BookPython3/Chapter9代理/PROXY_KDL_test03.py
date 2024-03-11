# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_KDL_test03.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/7 9:44 
"""
'''
快代理 隧道代理
'''
import requests

url = 'http://www.httpbin.org/ip'

# 代理信息
proxy_host = 'tps136.kdlapi.com'
proxy_port = '15818'
proxy_username = 't17260533422646'
proxy_password = 'v93cq4tk'

proxy = f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
proxies = {
    'http': proxy,
    'https': proxy
}

response = requests.get(url, proxies=proxies)
print(response.text)