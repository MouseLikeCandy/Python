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

# 定义一个实现数据过滤的函数
'''
def my_filter(tag):  # 默认就会接收一个tag类型的参数
    # 过滤数据
    bool = tag.name == 'a' and tag.has_attr('href')
    return bool
'''


# 定义一个实现数据过滤的函数
# 需求: 通过函数查找可以查找到一些复杂的节点元素, 查找文本值以'cie'结尾的所有<a>节点
def my_filter(tag):  # 默认会接受一个tag类型的参数
    print(tag)
    flag = False
    if tag.name == 'a':
        if len(tag.text) >= len('cie'):
            # 切片
            substring = tag.text[len(tag.text) - len('cie')]
            flag = substring == 'cie'  # 说明: 如果切出来的子串是cie, 此时flag就会重新赋值,这个值就是true
    return flag


# 需求: 查找class='story'的p标签
def my_filter2(tag):  # 默认会接受一个tag类型的参数
    print(tag)
    # class 可以拥有多个属性值  <p class='a b c'></p>
    # if tag.name == 'p' and tag['class'] == 'story':
    if tag.name == 'p' and tag['class'] == ['story']:   # 属性值写成列表的形式
        return True
    return False


response = urllib.request.urlopen('http://127.0.0.1:5000')
html = response.read().decode()

# 将页面转换为文档树类型
soup = BeautifulSoup(html, 'html.parser')

# 需求: 查找b标签的所有父标签  在test.html中<b>代替<title>标签后进行寻找
tag = soup.find('b')
print(tag)
print('-' * 100)
# 查找指定标签的父标签
parent = tag.parent
print(parent)
print('-' * 100)
# 找到顶层父标签
# Python 中条件为假的情况: ①None ②空字符串 ③0
while tag:
    # 查找指定标签的父标签
    print(tag.name)  # 标签名称
    # 一定要重新赋值
    tag = tag.parent
print('-' * 100)

# 获取 a 标签的属性值
tags = soup.find_all('a')
for tag in tags:
    print(tag['href'])  # a标签的属性href 超文本引用(hypertext reference)
    print(tag.text)  # 标签文本其实就是tag对象内部的text属性
    print(tag.get_text())  # get_text()这是tag对象提供的获取属性的方法

# 标签中的回车和空格, 其实都是对应标签的'文本数据', 可以用正则去掉
tags = soup.find_all('p')
for tag in tags:
    print(tag.text.strip())  # tag.text返回的是字符串类型的数据, strip()是字符串类型的方法, 作用是去除首位空格与回车

# 高级查找
# 使用一个函数名称替代条件过滤
# my_filter是什么呢? 是一个函数名称, 注意,千万不要写小括号, 因为加上小括号就是调用函数了
tags = soup.find_all(my_filter)  # 只能写过滤函数的名称,不能调用. 因为这个过滤是BeautifulSoup底层在合适的时机内部自己调用的.
print('--my_filter--')
for tag in tags:
    print(tag.text)

tags = soup.find_all(my_filter2)
print('--my_filter2--')
for tag in tags:
    print('tag.text', tag.text)
'''
父标签 子标签
'''
