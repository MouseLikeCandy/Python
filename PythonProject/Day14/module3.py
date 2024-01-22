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

# 第二种方式: 使用时, 不需要加上 包名.模块名, 可以直接使用该变量
# 阅读性不好
from Day14.module1 import x, y

# sys, random, math, time, datetime, calendar, ...Python语言的内置模块
# import sys      # sys.exit()
from sys import exit
# import random   # random.randint(1, 4)
from random import randint

# 方式三: 名字重复/名字过长  使用as取别名
# 如果自己模块与导入模块存在相同的变量, 如何处理?
from Day14.module1 import z as z2   # 更短的别名
z = '你好, 世界!'


if __name__ == '__main__':
    print(x)
    print(y)
    print(z2)
    print(z)
    randint(1, 4)
    # 说明: xxx 和 类.xxx 可能存在于两个不同的模块.
    # 类本身有一些自己的行为,执行完毕后,该方法可能会直接执行内置的xxx行为.
    exit(0)