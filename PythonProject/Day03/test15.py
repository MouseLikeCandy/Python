# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 21:56
@Auth ： 异世の阿银
@File ：test15.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 需求：求出1 ~ 100之间所有整型数值累加和
# 为了实现循环内部的数值类型，我们需要一个‘框’变量，用于累加循环中每一个整型数值
# 注意：这个框变量，我们仅需要一个，千万不要定义在循环体中

# 定义一个'框'变量
sum = 0
# 1.定义一个循环变量
i = 1
# 2.定义循环变量
while i <= 100:
    print(i, end='\t')
    sum += i
    i += 1

print(f'sum = {sum}')