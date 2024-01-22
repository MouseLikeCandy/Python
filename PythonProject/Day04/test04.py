# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 6:26
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 使用for 循环，求1~100之间所有整数的累加和

# 1.定义一个框变量
sum = 0

for i in range(1, 101):
    # print(i, end='\t')
    # 将当前i对应的整型数值累加到框变量中
    sum += i

# 当前循环结束后，查看‘框’变量中的累加和
print(f'sum = {sum}')