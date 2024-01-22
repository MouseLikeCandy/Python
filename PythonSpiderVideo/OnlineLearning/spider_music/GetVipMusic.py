# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/8 10:32
@Auth ： 异世の阿银
@File ：GetVipMusic.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import requests
from lxml import etree
# 将列表格式的字符串转为列表格式
import ast
import json
import time

import os
# 浏览器渲染界面和需要的不一样
# response = requests.get("https://music.163.com/#/discover/toplist")
response1 = requests.get("https://music.163.com/song?id=208891")
html_data1 = response1.text
# print(f'html_data1:{html_data1}, type:{type(html_data1)}')
with open('vip.txt', 'wb') as f:
    f.write(response1.content)
    f.close()


response2 = requests.get("https://music.163.com/#/song?id=1944644041")
html_data2 = response1.text
# print(f'html_data2:{html_data2}, type:{type(html_data2)}')
with open('not_vip.txt', 'wb') as f:
    f.write(response2.content)
    f.close()

