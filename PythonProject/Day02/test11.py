# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 21:01
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 比较运算符 ：比较两个数值之间的关系（大于 小于 大于等于  小于等于 等于== 不等于！=）
# 比较运算符只有两种结果 ： 非真即假， 非假即真  bool类型的返回结果
# 会不会存在’半真半假‘ 的情况？  不存在
num1 = 10
num2 = 20
result = num1 > num2
print(f'result = {result}，type(result) = {type(result)}')

n1 = 10
n2 = 10
# result = n1 = n2
result = n1 == n2
print(f'result = {result}')

