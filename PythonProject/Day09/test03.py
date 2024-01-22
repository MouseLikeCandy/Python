# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 20:04
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
    函数传参
#   关键字参数
#   round(*args(arguments), **kwargs(keyword arguments)):
#   说明: 字典数据实现关键字传递,需要加两颗星  **字典类型
'''


def function_math(a, b, c):
    result = a + b - c
    return result


# 位置传参, 参数个数保持一致
result = function_math(10, 20, 30)
print(f'result = {result}')

# 关键字传参, 使用key = value实现传递
result = function_math(c=10, b=20, a=30)  # 像字典key = value
print(f'result = {result}')

# 定义一个字典
num_dict = {'a': 30, 'b': 20, 'c': 10}
# 调用函数
# TypeError: function_math() missing 2 required positional arguments: 'b' and 'c'
# 类型错误: 缺失了两个必须传递未知参数
# 字典未被拆解
# result = function_math(num_dict)
# print(f'result = {result}')

# 如果传递的是字典数据,需要将字典数据拆解为关键字参数实现传递
result = function_math(**num_dict)
print(f'result = {result}')

# 说明: 字典数据实现关键字传递,需要加两颗星  **字典类型
