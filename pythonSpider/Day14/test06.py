# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 19:09
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
403 Forbidden   客户端不是浏览器不让访问

请求头headers
知乎搜索
'''

import requests


# 设置请求中的'请求代理'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
                  "X-Amzn-Trace-Id": "Root=1-6489988c-369241b710506fbe494991c2"
}

# 知乎网站的搜索请求地址
url = 'https://www.zhihu.com/explore'
# 之前写法:
# 1. 创建一个请求对象 request = urllib.request.Request(url, headers)
# 2. 发送请求        response = urllib.request.urlopen(request)
response = requests.get(url, headers=headers)
print(response.text)
