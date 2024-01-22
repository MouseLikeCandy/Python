# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 18:16
@Auth ： 异世の阿银
@File ：client.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
不用浏览器, 自己做客户端
'''
import urllib.request
from bs4 import BeautifulSoup


# 说明: 程序自己编写的客户端, 如果页面中有 JS 异步请求, 是不会自动发送请求的, 所以看不到数据
# 请问: 以下代码总共发送了几个请求??? 1个   浏览器总共发送两个请求 (网络-全部)
response = urllib.request.urlopen('http://127.0.0.1:5000')
html = response.read().decode()
print(html)     # 和phone的数据一模一样, 而浏览器中查看元素是有数据的

'''
<span id="jMsg"></span> <br />
<span id="sMsg"></span> <br />
'''

'''
浏览器中能看到的数据都是可以爬取的
'''

# 开始爬取
# 将页面封装为一个文档树对象
soup = BeautifulSoup(html, 'html.parser')
hMsg = soup.find('span', attrs={'id': 'hMsg'}).text
jMsg = soup.find('span', attrs={'id': 'jMsg'}).text
sMsg = soup.find('span', attrs={'id': 'sMsg'}).text
print(f'hMsg = {hMsg}')     # hMsg = Html Message
print(f'jMsg = {jMsg}')     # jMsg =
print(f'sMsg = {sMsg}')     # sMsg =

# 浏览器看到数据, 自己的客户端拿不到数据
#