# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:57
@Auth ： 异世の阿银
@File ：str_split.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 逗号表达式

# n1 = 10
# n2 = 20
# n3 = 30

# 同时定义三个变量


# ValueError: too many values to unpack (expected 3) 底层是元组解包的过程
# n1, n2, n3 = 10, 20, 30, 40

# Python语言的写法，两种含义一样
n1, n2, n3 = (10, 20, 30)
n1, n2, n3 = 10, 20, 30
print(f'n1 = {n1}, n2 = {n2}, n3 = {n3}')
