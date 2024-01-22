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

dayup = math.pow(1.01, 365)
daydown = math.pow(0.99, 365)

print(dayup, daydown)
print('dayup = {0: .2f}, daydown = {1: .2f}'.format(dayup, daydown))

dayup = math.pow(1.001, 365)
daydown = math.pow(0.999, 365)

print(dayup, daydown)
print('dayup = {0: .2f}, daydown = {1: .2f}'.format(dayup, daydown))
