# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 21:42
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 遍历 33 ~ 99 之间的所有整型数值
# 遍历 ： 在指定范围内依次取出每一个整型数值的操作，我们称之为遍历

# 1.定义一个循环变量
i = 33
# 2.使用循环变量 + 循环增量控制循环条件
while i <= 99:
    # print(i)   # print()输出函数默认自动换行
    print(i, end='\t')

# 3.循环增量(让循环变量自增, 需要在循环体内)
    i += 1