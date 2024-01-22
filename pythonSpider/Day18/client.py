# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/12 20:26
@Auth ： 异世の阿银
@File ：client.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
其他页面中没有返回主页<a href="books.html">HOME</a>
深度优先算法
递归就是深度优先
'''
# 自定义一个函数, 一会需要递归调用
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse


def spider(url):
    # 发送请求
    response = urllib.request.urlopen(url)
    # 获取数据
    html = response.read().decode()
    # print(html)
    # 将数据转换为文档树类型
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find('h3').text
    print(text)
    # 获取页面中所有 a 超链接标签的 href 数值
    links = soup.select('a')
    for link in links:
        # 取出 link 中对应的 href 属性值
        href = link['href']
        # print(href)     # href 并不是一个完整的url

        # urllib.parse 请求的解析模块中有一个urljoin()方法可以只能完成url地址的拼接
        full_url = urllib.parse.urljoin(url, href)
        # print(full_url)

        # 再次发送请求
        spider(full_url)    # 直接使用递归调用


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/'

    spider(url)
