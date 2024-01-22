# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 20:48
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
    函数的参数可以设置默认值,如果有默认值的参数,调用的时候可以不传递,直接使用默认
    
'''

def get_sum(a, b=10):
# def get_sum(b=10, a):   # 非默认值参数跟随默认值参数 -- 拥有默认值的参数必须位于没有默认值的参数之后
    sum = a + b
    return sum


# 调用函数
result = get_sum(10)
print(f'result = {result}')

result = get_sum(10, 20)
print(f'result = {result}')