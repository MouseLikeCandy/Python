# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:30
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 算术运算符 ：+ - * /(除) //（整除） %（余数/取模）   **幂运算
num1 = 10
num2 = 3
result = num1 / num2
print(f'result = {result}')   # result = 3.3333333333333335 带小数,没有那么高的精确度

# 将小数部分直接舍弃
result = num1 // num2
print(f'result = {result}')

result = num1 % num2
print(f'result = {result}')

# 幂运算
result = num1 ** num2
print(f'result = {result}')   # 10 * 10 * 10



