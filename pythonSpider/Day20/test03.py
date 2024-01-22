# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/12 11:42
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import urllib.request
from bs4 import BeautifulSoup

'''
实例: 链家二手房(北京)
https://bj.lianjia.com/ershoufang/rs/
'''
# 创建链家爬虫类
class LianjiaSpider(object):
    # 初始化数据
    def __init__(self):
        '''
        https://bj.lianjia.com/ershoufang/
        https://bj.lianjia.com/ershoufang/pg2/
        https://bj.lianjia.com/ershoufang/pg3/
        https://bj.lianjia.com/ershoufang/pg4/
        '''
        self.url = 'https://bj.lianjia.com/ershoufang/pg{0}/'   # {0}第一个占位符, 后面可以使用format()函数拼接数据

    # 爬取数据的行为
    def crawl(self):
        for i in range(1, 2):
            full_url = self.url.format(i)
            # 发送请求
            self.send_request(full_url)

    # 发送请求
    def send_request(self, full_url):
        try:
            response = urllib.request.urlopen(full_url)
            # 获取页面数据
            html = response.read().decode()
            # print(html)
            # 解析数据
            soup = BeautifulSoup(html, 'html.parser')
            # 首先获取 ul 标签
            ul = soup.find('ul', attrs={'class': 'sellListContent'})
            # print(ul)
            # 从ul标签中获取所有的li标签
            lis = ul.find_all('li')
            # print(len(lis))
            # 遍历list列表
            for li in lis:
                # title
                title = li.find('div', attrs={'class': 'title'}).text
                # positionInfo
                positionInfo = li.find('div', attrs={'class': 'positionInfo'}).text
                # houseInfo
                houseInfo = li.find('div', attrs={'class': 'houseInfo'}).text
                # followInfo
                followInfo = li.find('div', attrs={'class': 'followInfo'}).text
                # totalPrice totalPrice2
                totalPrice = li.find('div', attrs={'class': 'totalPrice totalPrice2'}).text
                # unitPrice
                unitPrice = li.find('div', attrs={'class': 'unitPrice'}).text

                print(title, positionInfo, houseInfo, followInfo, totalPrice, unitPrice)

        except BaseException as e:
            print(e)

# 测试代码
if __name__ == '__main__':
    # 1. 创建链家爬虫对象
    spider = LianjiaSpider()
    # 2. 让 spider 执行 crawl 行为
    spider.crawl()