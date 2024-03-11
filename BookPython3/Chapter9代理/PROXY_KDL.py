# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_KDL.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/7 9:08 
"""

'''
快代理 测试
'''
import requests

PROXY_API = 'https://dps.kdlapi.com/api/getdps/?secret_id=ozv4dpm3ox90zo7ku2sd&num=10&signature=68bvtk2bxh7y1pd4kku9kycci27njay9&pt=1&sep=1'

def get_proxies():
    response = requests.get(PROXY_API)
    return response.text.split('\n')

def test_proxies():
    proxies = get_proxies()
    for proxy in proxies:
        proxy = proxy.strip()
        print(f'using proxy {proxy}')
        try:
            response = requests.get('http://www.httpbin.org/ip', proxies={
                'http': 'http://' + proxy
            })
            print(response.text)
        except requests.ConnectionError:
            print(f'proxy {proxy} is invalid')


if __name__ == '__main__':
    test_proxies()
