# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/24 21:09
@Auth ： 异世の阿银
@File ：client7.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.request
from bs4 import BeautifulSoup

'''
子孙标签 descendants
'''


# d定义一个实现数据过滤的函数
def my_filter(tag):  # 默认就会接收一个tag类型的参数
    # 过滤数据
    bool = tag.name == 'a' and tag.has_attr('href')
    return bool

    # 需求: 通过函数查找可以查找到一些复杂的节点元素, 查找文本值以'cie'结尾的所有<a>节点
    flag = False
    if tag.name == 'a':
        if len(tag.text) >= len('cie'):
            # 切片
            substring = tag.text[len(tag.text) - len('cie')]
            flag = substring == 'cie'  # 说明: 如果切出来的子串是cie, 此时flag就会重新赋值,这个值就是true
    return flag


response = urllib.request.urlopen('http://127.0.0.1:5000')
html = response.read().decode()

# 将页面转换为文档树类型
soup = BeautifulSoup(html, 'html.parser')
# 获取 a 标签的属性值
tags = soup.find_all('a')
for tag in tags:
    print(tag['href'])
    print(tag.text)  # text是tag对象内部的属性
    print(tag.get_text())  # get_text()这是tag对象的方法

# 标签中的回车和空格, 其实都是对应标签的'文本数据'
tags = soup.find_all('p')
for tag in tags:
    print(tag.text.strip())  # tag.text返回的是字符串类型的数据, strip()是字符串类型的方法, 作用是去除首位空格与回车

# 高级查找
# 使用一个函数名称替代条件过滤
# my_filter是什么呢? 是一个函数名称, 注意,千万不要写小括号, 因为加上小括号就是调用函数了
tags = soup.find_all(my_filter)  # 只能写过滤函数的名称,不能调用. 因为这个过滤是BeautifulSoup底层在合适的时机内部自己调用的.
for tag in tags:
    print(tag.text)

# 需求: class='story'下p标签的所有子标签
tag = soup.find('p', attrs={'class': 'story'})
print(tag.children)

for tag in tag.descendants:  # 表示指定标签的子孙标签, 将子标签中的数据作为孙子标签
    print(tag)
    print('-' * 100)


