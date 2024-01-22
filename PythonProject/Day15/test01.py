# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 12:45
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
Python内置模块
'''
import time

# 查看time模块中的所有属性
print(dir(time))

# 查看time模块中关于time的具体使用 -> help
help(time.time)

# 查看time返回的结果
seconds = time.time()
print(f'seconds = {seconds}')   # 16亿多秒, 格林威治时间 1970年1月1日0:0:0开始计时