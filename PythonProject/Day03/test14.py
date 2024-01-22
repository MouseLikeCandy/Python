# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 21:49
@Auth ： 异世の阿银
@File ：test14.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 找出 1 ~ 100 之间的偶数

'''
# tab 水平制表符 向右缩进
# shift 水平制表符 向左缩进
'''

# 1。定义变量
i = 1

# 2.指定循环条件
while i <= 100:
    if i % 2 == 0:
        print(i, end='\t')   # print默认自动换行，使用end改变格式
# 3.循环增量
    i += 1  # 小心缩进
