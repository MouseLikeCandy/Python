# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 19:17
@Auth ： 异世の阿银
@File ：str_split.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


'''
* 
* * 
* * * 
* * * * 
* * * * * 
切开
* * * * 
* * * 
* * 
* 

'''

# 这是第一个循环嵌套
for i in range(1, 6, 1):
    for j in range(i):
        print('*', end=' ')
    print()

# 又是一个新的循环嵌套
for i in range(4):
    for j in range(4 - i):
        print('*', end=' ')
    print()     # print(end='\n')
