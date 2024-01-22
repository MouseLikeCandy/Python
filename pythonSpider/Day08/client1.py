# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/3 19:43
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import os
import urllib.request
import urllib.parse

'''
上传数据 
'''

# url请求地址
url = 'http://127.0.0.1:5000/upload'  # 上传路由

# 提示用户输入一个文件路径
filename = input('Enter the file: ')     # 输入文件路径C:\Users\YiNing\Desktop\gym.jpg

# 判断文件是否存在
if os.path.exists(filename):
    print(filename)
    # 获取路径中的文件名称
    name = os.path.basename(filename)
    print(name)
    # 读取数据
    with open(filename, 'rb') as f:
        data = f.read()     # 二进制数据

    # 发送请求
    url = url + f'?filename=' + urllib.parse.quote(name)


    # http协议规定， 上传需要携带以下’field字段/名称/属性‘
    # 1. 上传的请求头
    headers = {'content-type': 'application/octet-stream'}  # 内用类型： 应用 八进制数据流

    # 2. 设置自定义请求头对象
    request = urllib.request.Request(url, data, headers)  # data是post请求
    # 3. 发送请求
    response = urllib.request.urlopen(request)  # 一个请求对应一个响应对象
    # 4. 判断是否上传成功
    msg = response.read().decode()
    print(msg)
    if msg == 'OK':
        print('上传成功！')
    else:
        print(msg)
else:
    # 文件不存在
    print('亲, 该文件不存在, 无法上传!')



