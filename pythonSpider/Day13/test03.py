# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/13 7:14
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
模拟网页, 在本地爬取
'''
import urllib.request
import bs4
from bs4 import BeautifulSoup

url = 'https://www.shanghairanking.cn/rankings/bcur/2023'

# url = 'http://127.0.0.1:5000/'
response = urllib.request.urlopen(url)
html = response.read().decode()
soup = BeautifulSoup(html, 'html.parser')

# 解析数据
# 回顾: children 实现解析的时候, 会将回车, 空格 都作为子元素
trs = soup.find('tbody').children   # trs是一个 list_iterator对象, 不能使用len()方法
# 遍历trs
for tr in trs:
    # print(type(tr), tr)     # <class 'bs4.element.NavigableString'>  <class 'bs4.element.Tag'>
    # children 获取的数据中有可能出现导航字符串, 就是回车和空格, 我们不需要
    # 判断 bs4.element.Tag
    if isinstance(tr, bs4.element.Tag):
        # 取数据
        # print(tr)
        print('_' * 100)
        # 获取每一个tr中的所有td标签
        # tds = tr('td')
        tds = tr.find_all('td')
        # 排名
        ranking = tds[0].text.strip()
        # 大学名称
        # university = tds[1].text.strip()
        university_name = tds[1].find('a', attrs={'class': 'name-cn'}).text.strip()     # attrs
        # 省份
        province = tds[2].text.strip()
        # 类型
        typing = tds[3].text.strip()
        # 总分
        score = tds[4].text.strip()
        # 办学层次
        education_level = tds[5].text.strip()

        print(ranking, university_name, province, typing, score, education_level)

# 下一个版本, 面向对象, 数据存到数据库中.


