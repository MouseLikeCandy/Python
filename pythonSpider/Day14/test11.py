# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 19:37
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
案例练习: 国家地理图片
'''

import requests
import os

url = 'http://img0.dili360.com/ga/M02/33/7C/wKgBzFSbqQyAJVAuAARB8cSWH_w695.tub.jpg'
# 先将url地址中的文件名称取出
img_name = os.path.basename(url)
# 将图片资源存储到当前项目的static文件夹
if not os.path.exists('static'):
    os.mkdir('static')
# 发送请求存储文件
response = requests.get(url)
print(response.status_code)

# 二进制数据直接保存
with open('static/' + img_name, mode='wb') as f:
    f.write(response.content)

print('completed !')
