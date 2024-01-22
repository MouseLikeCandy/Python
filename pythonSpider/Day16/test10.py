# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 22:55
@Auth ： 异世の阿银
@File ：test10.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re

if __name__ == '__main__':
    regEx = r'\d+'
    str = 'abcd123efghi5645jklm432no324pqrs789tuvwxyz'

    # 方式一: re.findall(正则字符串, 源数据)
    numbers = re.findall(regEx, str)
    for num in numbers:
        print(num)

    # 方式二:
    # 1. 将正则字符串编译为正则对象
    pattern = re.compile(regEx)
    print(type(pattern))

    # 2. 正则对象调用正则方法
    nums = pattern.findall(str)

    # 3. 查看结果
    for num in numbers:
        print(num)

    print('-' * 100)

    str2 = 'BJ100100 SH100200 GZ100300 SZ100400'
    numbers = pattern.findall(str2)
    for num in numbers:
        print(num)