# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 20:05
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 列表生成器

# 需求：生成一个列表：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list)

# range()  范围函数
# range(1, 11, 1)

num2_list = [i for i in range(1, 11, 1)]
print(num2_list)

# 需求： [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num3_list = [i * 10 for i in range(1, 11, 1)]
print(num3_list)

for i in range(10, 101, 10):
    print(i, end='')

num4_list = [i for i in range(10, 101, 10)]
print(num4_list)

for i in range(1, 11, 1):
    print(i ** 2)
# 需求： [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num5_list = [i ** 2 for i in range(1, 11, 1)]
print(num5_list)

# 需求： [3, 6, 9, 12, 15, 18, ... , 99]

for i in range(3, 100, 3):
    print(i, end= '\t')

num6_list = [i for i in range(3, 100, 3)]
print(num6_list)

# for i in range(1, 100, 1):
#     if i % 3 == 0:
#         print(i, end='\t')

num7_list = [i for i in range(1, 100, 1) if i % 3== 0]
print(num7_list)

