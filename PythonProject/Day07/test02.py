# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 20:17
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 1. + 可以将两个列表拼接为一个列表
# 会返回一个新的列表，定义变量实现新列表的接收
num1_list = [10, 20, 30]
num2_list = [40, 50, 60]
new_list = num1_list + num2_list
print(num1_list)
print(num2_list)
print(new_list)
# 2. * 可以将列表重复指定的次数
new_list2 = num1_list * 3
print(num1_list)
print(new_list2)
# 3. min() 获取列表中的最小值
num_list = [55, 88, 44, 43, 11, 99, 23]
min = min(num_list)
print(min)
# 4. max()
max = min(num_list)
print(max)

# 5. 列表.count(元素)
count = num_list.count(43)
print(f'count = {count}')

