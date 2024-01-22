# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 22:07
@Auth ： 异世の阿银
@File ：exam01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 练习：部门业绩 -> 公司业绩
list_data = [[11, 12], [21, 22, 23], [31, 32, 33, 34]]
print(list_data)

total = 0
for i in range(len(list_data)):
    department = list_data[i]
    print(f'部门{i + 1}的业绩列表：{department}')
    count = 0
    for performance in department:
        count += performance
        total += performance
    print(f'部门{i + 1}的业绩总额：{count}')
print(f'公司的业绩总额：{total}')




