# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:50
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 点击代码区左侧的边栏，实现’端点breakpoint‘定义   debug运行   F7
n = 10
n += 1
print(f'n = {n}')

n -= 5
print(f'n = {n}')

n *= 5
print(f'n = {n}')

n /= 5
print(f'n = {n}')

n %= 5
print(f'n = {n}')

# 强调：变量可以实现反复赋值，但是要小心。
# 新值会覆盖原来的旧值
