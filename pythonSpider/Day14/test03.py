# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 18:36
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
httpbin.org 这个网站能够测试HTTP请求和响应的各种信息
比如cookie,IP,headers和登录验证等

浏览器访问httpbin.org 
http://httpbin.org/get  测试get请求
返回一个json格式的数据类型
{
  "args": {},       get请求参数
  "headers": {      http协议请求头
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43", 
    "X-Amzn-Trace-Id": "Root=1-6489988c-369241b710506fbe494991c2"   用户代理(浏览器)
  }, 
  "origin": "182.200.11.10",    服务商地址, 通过这个IP地址发送出去的
  "url": "http://httpbin.org/get"
}
'''

import requests


# 发送一个get请求
response = requests.get('http://httpbin.org/get?name=jack&age=18')

print(response.text)
'''
{
  "args": {
    "age": "18", 
    "name": "jack"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.27.1",     客户端, 非浏览器, 爬取数据时修改这个值
    "X-Amzn-Trace-Id": "Root=1-648999ed-16f4c09d47a3cab9636a0d11"
  }, 
  "origin": "182.200.11.10", 
  "url": "http://httpbin.org/get?name=jack&age=18"
}
'''
