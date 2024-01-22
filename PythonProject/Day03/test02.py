# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 20:07
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 判断3个整型数值中的最大值

# 定义变量，接收用户的输入

num1 = int(input('亲，请输入第一个整型数值：'))
num2 = int(input('亲，请输入第二个整型数值：'))
num3 = int(input('亲，请输入第三个整型数值：'))

# 逻辑判断
if num1 > num2:
    # num1大
    if num1 > num3:
        # num1最大
        print(f'num1 = {num1}')
    else:
        # num3最大
        print(f'num1 = {num3}')
else:
    # num2大
    if num2 > num3:
        # num2最大
        print(f'num1 = {num2}')
    else:
        # num3最大
        print(f'num1 = {num3}')
