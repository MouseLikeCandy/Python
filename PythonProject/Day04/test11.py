# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 19:33
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 需求： 输出九九乘法表

# 外层循环：9行
for i in range(9):
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(9):
    for j in range(i + 1):
        print(f'{j + 1} * {i + 1} = {(i + 1) * (j + 1)}', end=' ')
    print()

for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()


