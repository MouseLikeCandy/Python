# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/22 20:27
@Auth ： 异世の阿银
@File ：client2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
客户端下载
'''
import urllib.request
import urllib.parse
import os

url = 'http://127.0.0.1:5000/'

# 发送请求
response = urllib.request.urlopen(url)  # 这个请求中没有携带filename这个key
resource_list = response.read().decode()

print(resource_list)

filename = input('亲, 请输入需要下载的资源名称: ')
filename = urllib.parse.quote(filename)  # 处理中文名称可能出现的错误问题

# 再次发送请求
url = url + f'?filename={filename}'  # get请求一定加问号
# url = 'http://127.0.0.1:5000/?filename=3.JPG'
response = urllib.request.urlopen(url)
# msg = response.read().decode()
# print(msg)
data = response.read()
print(data)

# 客户端的需求: 将从服务端下载的图片保存到download文件夹中
if not os.path.exists('download'):
    os.mkdir('download')

# 将数据保存到文件夹中
with open('download/' + filename, 'wb') as f:
    f.write(data)

print(f'下载完毕: {filename}, 字节数: {len(data)}')

