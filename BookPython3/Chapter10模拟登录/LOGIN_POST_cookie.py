# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：LOGIN_POST_cookie.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/8 9:37 
"""
import requests
from urllib.parse import urljoin
'''
模拟登录的关键在于两次发出的请求的Cookie相同。
因此可以把第一次登录后的Cookie保存下来，在第二次请求的时候加上这个Cookie.
'''

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, allow_redirects=False)   # 使requests不自动处理重定向

cookies = response_login.cookies     # 保存第一次请求的cookie
print('Cookies', cookies)


response_index = requests.get(INDEX_URL, cookies=cookies)   # 再次发送请求时带上cookies
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)   # 登录失败，返回登录页面
