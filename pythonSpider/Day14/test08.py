# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 19:19
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
requests库post请求
设置headers, 骗服务器我不是客户端
'''
import requests

url = "http://httpbin.org/post"

# 定义post请求需要传递的数据
data = {
    'name': 'jack',
    'age': 18
}

# 设置请求中的'请求代理'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "X-Amzn-Trace-Id": "Root=1-6489988c-369241b710506fbe494991c2"
}

# 之前写法
# urllib.request.urlopen(url + ?key=value&key=value, data=data)
response = requests.post(url, data=data, headers=headers)
print(response.text)
'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {             数据存在数据表单form中
    "age": "18", 
    "name": "jack"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "16", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.27.1", 
    "X-Amzn-Trace-Id": "Root=1-6489a31a-155e602826bbe89901a62b52"
  }, 
  "json": null, 
  "origin": "182.200.11.10", 
  "url": "http://httpbin.org/post"
}
'''