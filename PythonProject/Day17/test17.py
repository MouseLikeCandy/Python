# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 21:52
@Auth ： 异世の阿银
@File ：test17.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from Day17.model import Student
import shelve

if __name__ == '__main__':
    # 1. 打开shelve
    stus = shelve.open('stus')
    # 2. 访问数据
    for key, value in stus.items():
        print(key, value)

    # 3. 关闭shelve
    stus.close()