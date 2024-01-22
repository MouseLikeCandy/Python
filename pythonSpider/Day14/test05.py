# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 19:02
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
www.github.com
下载网站首页图标 favicon.ico
'''

import requests

# url = 'http://www.github.com/favicon.ico'
url = 'https://www.sina.com.cn/favicon.ico'
response = requests.get(url)
# 之前用 response.read() 二进制数据
print(response.content)    # 二进制数据不是用来看的, 不可能看得懂.

# 实现: 将二进制数据直接保存为固定类型的文件
with open('favicon.ico', mode='wb') as f:
    f.write(response.content)

print('compeleted!')