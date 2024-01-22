# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 6:47
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 输出一个直角三角形

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

# 1.外层循环控制行，总共5行

for i in range(5):
    # 2.内层循环控制列，列是变化的，不是固定的
    for j in range(i + 1):
        print('*', end='')
    print()

# 1.外层循环控制行，总共5行

for i in range(1, 6):
    # 2.内层循环控制列，列是变化的，不是固定的
    for j in range(i):
        print('*', end=' ')
    print()

