# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 9:14
@Auth ： 异世の阿银
@File ：module2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 需要使用module1模块下的变量

# 如何导入包中的模块?
# 即使模块在同一包下, 也需要指定包名

# 第一种方式: 使用时, 必须加上 包名.模块名
import Day14.module1

# sys, random, math, time, datetime, calendar, ...Python语言的内置模块
import sys      # sys.exit()
import random   # random.randint(1, 4)

def method_two():
    print('这是module2的method_two方法')

if __name__ == '__main__':
    print(Day14.module1.x)
    print(Day14.module1.y)
    print(Day14.module1.z)
    random.randint(1, 4)