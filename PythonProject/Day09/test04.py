# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 20:37
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 复杂的函数参数定义
# args -> arguments  形式参数 / 位置参数
# kwargs -> keyword arguments 关键字参数
# 说明: 关键字参数必须位于位置参数之后

#positional_argument                    位置参数
#positional_or_keyword_argument         位置参数和关键字参数
#keyword_argument                       关键字参数
'''


def function_args(n1, n2, n3, *args, **kwargs):
    print(f'n1 = {n1}')
    print(f'n2 = {n2}')
    print(f'n3 = {n3}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    return


# 调用函数
function_args(10, 20, 30, 40, 50, 60, 70, a=80, b=90, c=100)

# 错误定义函数
# def function_args(*args, n1, n2, n3, **kwargs):
#     print(f'n1 = {n1}')
#     print(f'n2 = {n2}')
#     print(f'n3 = {n3}')
#     print(f'args = {args}')
#     print(f'kwargs = {kwargs}')
#     # 报错: 一个星的参数必须位于两个星的参数之后了
# def function_args(n1, n2, n3, **kwargs, *args):
#     print(f'n1 = {n1}')
#     print(f'n2 = {n2}')
#     print(f'n3 = {n3}')
#     print(f'args = {args}')
#     print(f'kwargs = {kwargs}')
