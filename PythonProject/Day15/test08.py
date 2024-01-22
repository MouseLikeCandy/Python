# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 14:25
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
math

# 思考: 每天进步一点点, 一年后有什么变化? (百分之一,千分之一)
#       每天退步一点点, 一年后有什么变化?
# 持续的力量
'''

import math

print(dir(math))

# 平方根函数
print(math.sqrt(2))

# 对数
print(math.log(8, 2))

# 幂函数
print(math.pow(2, 3))

# 圆周率
print(math.pi)


# 取整的函数 ceil(天花板)  floor(地板)
print(math.ceil(8.1))   # 向上取整
print(math.floor(8.1))  # 向下取整


# 四舍五入
print(round(4.4))
print(round(4.5001))    # 至少保留两位有效小数

dayup = math.pow(1.01, 365)
daydown = math.pow(0.99, 365)

print(dayup, daydown)
print('dayup = {0: .2f}, daydown = {1: .2f}'.format(dayup, daydown))


dayup = math.pow(1.001, 365)
daydown = math.pow(0.999, 365)

print(dayup, daydown)
print('dayup = {0: .2f}, daydown = {1: .2f}'.format(dayup, daydown))