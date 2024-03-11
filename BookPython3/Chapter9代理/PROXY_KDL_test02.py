# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROXY_KDL_test02.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/7 9:39 
"""
"""
使用requests请求代理服务器
请求http和https网页均适用

快代理 通过接口提取代理
"""

import requests

# 提取代理API接口，获取1个代理IP
api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=ozv4dpm3ox90zo7ku2sd&num=10&signature=68bvtk2bxh7y1pd4kku9kycci27njay9&pt=1&sep=1"

# 获取API接口返回的代理IP
proxy_ips = requests.get(api_url).text.split('\n')

# # 用户名密码认证(私密代理/独享代理)
# username = "d1451877865"
# password = "vs2uug40"
# 要访问的目标网页
target_url = "https://dev.kdlapi.com/testproxy"
for proxy_ip in proxy_ips:
    proxy_ip = proxy_ip.strip()
    # proxies = {
    #     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    #     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
    # }

    # 白名单方式（需提前设置白名单）
    proxies = {
        "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
        "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
    }

    # 使用代理IP发送请求
    response = requests.get(target_url, proxies=proxies)

    # 获取页面内容
    if response.status_code == 200:
        print(response.text)