# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/12 18:32
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
案例: 爬取天气网
http://www.weather.com.cn/

北京 七天数据

客户端: 发送请求, 获取响应, 实现数据分析

'''

import urllib.request
from bs4 import BeautifulSoup

# 异常处理
try:
    # 1. 确认请求的url地址
    url = 'http://www.weather.com.cn/weather/101010100.shtml'   # 北京代码 101010100
    url = 'http://www.weather.com.cn/weather/101070101.shtml'   # 沈阳代码 101070101
    # 2. 发送请求
    response = urllib.request.urlopen(url)
    # 3. 获取响应中的数据
    html = response.read().decode()
    print(html)
    # 确认获取的数据和浏览器看到的数据是一致的.
    # 网页上右键 - 检查 - 鼠标箭头图标(第一个, 桌面端页面结构) - 选择页面 - 找到标签
    # 两个框框图标(第二个, 移动端页面结构)

    # 4. 将html字符串类型的数据转换为'文档树'结构
    soup = BeautifulSoup(html, 'html.parser')
    print('-' * 100)
    print(soup)
    # 5. 使用soup对象实现页面解析
    lis = soup.select('ul[class="t clearfix"] > li')    # select()方法返回的是一个列表
    print(f'len = {len(lis)}')
    # 6. 遍历列表
    for li in lis:      # li的类型也是bs4.element.tag 标签类型, 因此依然可以调用 'find, find_all, select' 方法查找数据
        # 去浏览器分析
        # 6.1 日期
        date = li.select('h1')[0].text     # select()方法返回的数据哪怕只有一条数据也是列表类型, 因此取数据时使用下标.
        # 6.2 天气
        weather = li.select('p[class="wea"]')[0].text
        # 6.3 温度
        temperature = li.select('p[class="tem"]')[0].get_text().strip()   # 只取外层的p标签, 去除数据首尾空格和换行
        # 6.4 风力
        wind = li.select('p[class="win"] > i')[0].text
        print(date, weather, temperature, wind)

except BaseException as e:
    print(e)
