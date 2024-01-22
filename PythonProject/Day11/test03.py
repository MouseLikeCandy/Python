# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/8 6:27
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 补充
# 关于编程语言中的int类型:
C, Java, JS, OC, Swift ...定义整形int(4个字节, 32比特位), long(8个字节,64比特位)
32比特位: 21亿~ -21亿(总共可以存储42亿大的数据)

Python中没有int 和long 区分, 理论上支持无限大的数字.
Python使用动态长度
Python应用领域:
1. 科学计算
2. 机器学习
3. 人工智能
'''

import sys
print(sys.getsizeof(0))  # 24字节
print(sys.getsizeof(1))  # 28字节
print(sys.getsizeof(2))  # 28字节
print(sys.getsizeof(2**15))  # 28字节
print(sys.getsizeof(2**30))  # 32字节
print(sys.getsizeof(2**60))  # 36字节
print(sys.getsizeof(2**60-1))  # 32字节
