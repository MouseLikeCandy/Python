# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 14:11
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
时间上的加减法
timedelta 方法, 表示两个时间点的间隔
'''

import datetime


now = datetime.datetime.now()
print(f'now = {now}')

yesterday = now - datetime.timedelta(days=1)
print(f'yesterday = {yesterday}')

tomorrow = now + datetime.timedelta(days=1)
print(f'tomorrow = {tomorrow}')

# 8天后是哪一天?
day = now + datetime.timedelta(days=8)
print(f'day = {day}')




