# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:22
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
字符串，整型，浮点型之间的数据转换：
格式：
1.整型int(变量)
2.浮点型float(变量)
3.字符串str(变量)
'''
num1 = 10
num2 = 20
sum1 = num1 + num2
print(f'sum = {sum1}')

# 字符串相加  拼接
num1 = '10'
num2 = '20'
sum1 = num1 + num2
print(f'type(sum1) = {type(sum1)}')
print(f'sum1 = {sum1}')

# 需求：将字符串转为整数类型
n1 = int(num1)
n2 = int(num2)
sum2 = n1 + n2
print(f'type(sum2) = {type(sum2)}')
print(f'sum2 = {sum2}')

s = str(sum2)
print(f"s={s},type(s)={type(s)}")

# 实现浮点数的减法
f1 = '10.5'
f2 = '5.5'
sub = f1 - f2
print(f'sub = {sub}')


