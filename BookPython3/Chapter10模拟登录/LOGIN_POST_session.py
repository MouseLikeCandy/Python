# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：LOGIN_POST_session.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/3/11 8:36 
"""
import requests
from urllib.parse import urljoin
'''
Session
'''

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

session = requests.session()

response_login = session.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, allow_redirects=False)   # 使requests不自动处理重定向

cookies = session.cookies     # 保存第一次请求的cookie
print('Cookies', cookies)


response_index = session.get(INDEX_URL)   # 再次发送请求时带上cookies
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)   # 登录失败，返回登录页面