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
'''

import requests


# 发送一个get请求
response = requests.get('http://httpbin.org/get?name=jack&age=18')

print(response.text)
print(type(response.text))
# 获取文本数据
text = response.text
# 将字符串转为字典类型    之前用json.loads(text)
dict_data = response.json()  # 没有修改text原本数据, 返回一个修改后的数据
print(dict_data)
print(type(dict_data))

# 需求: 取出 'User-Agent' key 对应的value值
# 说明: dict_data是一个字典, headers也是一个字典
print(f'type(dict_data["headers"]) = {type(dict_data["headers"])}')
print(dict_data['headers']['User-Agent'])
# print(dict_data.headers['User-Agent'])      # 如果可以这样写, 意味着可以使用面向对象的方法操作字典. 显然不可以.

