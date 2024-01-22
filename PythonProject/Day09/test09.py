# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 21:15
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    递归函数: recursion
    什么是递归?在一个函数体中, 调用了该函数本身.递归就是自己调用自己
    
    递归实现的注意点:
    ①一定要考虑清楚,如何结束死递归. -> 添加条件,让这个递归调用不再调用自己
    
    递归深度调用限制, 默认1000次
'''
import sys


def say_hi():
    print(f'大家好!, 我是Python')
    # 自己调用自己
    say_hi()

# 一个'死递归'

# 主函数
if __name__ == '__main__':

    # 获取递归深度(次数)
    limit = sys.getrecursionlimit()
    print(limit)
    # 修改递归限制
    sys.setrecursionlimit(3000)
    limit = sys.getrecursionlimit()
    print(limit)
    # 自定义函数只有被调用才会执行
    say_hi()
    print(f'程序继续向下执行...')

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 递归错误: 在调用Python对象时,达到了递归调用的最大深度.

