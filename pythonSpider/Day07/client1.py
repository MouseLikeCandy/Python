# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 22:09
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
Python 语言中已经为我们提供了http协议的请求库 urllib
urllib.request 请求模块
urllib.error 异常处理模块
urllib.parse url解析模块
urllib.robotparser robots.txt 解析模块
'''
import urllib.request

# 1.定义一个url请求地址
url = 'http://127.0.0.1:5000'

# 2.发送请求, http是一个请求响应模型, 一个请求必定会对应一个响应对象
# 默认发送get请求, 表单才能发送post请求
response = urllib.request.urlopen(url)


# 3.读取响应对象中的数据
# data = response.read()  # read()方法返回的是二进制数据
# data = response.read().decode('utf-8')
data = response.read().decode()     # 默认编码为utf-8
print(data)

