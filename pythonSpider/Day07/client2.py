# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 22:09
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
import urllib.parse

# 1.定义一个url请求地址
# url = 'http://127.0.0.1:5000/?province=广州&city=深圳'    # 汉字不能直接发送,需要数据转换 parse
# http://127.0.0.1:5000/?province=%E5%B9%BF%E5%B7%9E&city=%E6%B7%B1%E5%9C%B3
# get请求, 用浏览器访问 http://127.0.0.1:5000/?province=广州&city=深圳
url = 'http://127.0.0.1:5000'

# 准备参数  汉字转为字节数据
province = urllib.parse.quote('广州')
city = urllib.parse.quote('深圳')

data = f'?province={province}&city={city}'

print(url + data)

# 2.发送请求, 获取相应
response = urllib.request.urlopen(url + data)


# 3.机洗数据
data = response.read().decode()     # 默认编码为utf-8
print(data)

