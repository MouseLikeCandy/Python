# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 22:09
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''客户端post请求'''
import urllib.request
import urllib.parse

# 1.定义一个url请求地址
url = 'http://127.0.0.1:5000'

# 准备参数  汉字转为字节数据
province = urllib.parse.quote('广州')
city = urllib.parse.quote('深圳')

data = f'province={province}&city={city}'   # 字符串类型   以键值对的形式发送数据
print(type(data))

# 如何将字符串类型的数据转为字节类型的数据呢?
data = data.encode()    # encode()编码, 字符串 -> 字节类型
print(type(data))
# HTTP Error 405: METHOD NOT ALLOWED  405 不接收post请求, 修改服务端路由

# 2.发送请求, 获取相应
# urlopen() 如果传递第二个 data 数据的话, 说明当前请求就是post请求, 不是get请求.
# TypeError: POST data should be bytes   post请求传递的数据应该是一个bytes字节类型的数据.
response = urllib.request.urlopen(url, data)    # 两个参数  data是post数据 *************区别**************


# 3.解析数据
data = response.read().decode()     # 默认编码为utf-8
print(data)

