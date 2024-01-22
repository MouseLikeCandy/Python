# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 20:31
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 定义了一个列表嵌套
list_data = [[11, 12], [21, 22, 23], [31, 32, 33, 34]]

# 查看大整体
print(f'list_data[0] = {list_data[0]}')
print(f'list_data[1] = {list_data[1]}')
print(f'list_data[2] = {list_data[2]}')
print(f'len(list_data) = {len(list_data)}')

# 请问？： ‘11’这个元素如何获取？
print(f'list_data[0][0] = {list_data[0][0]}')
# 请问？： ‘23’这个元素如何获取？
print(f'list_data[1][2] = {list_data[1][2]}')
# 请问？： ‘32’这个元素如何获取？
print(f'list_data[2][1] = {list_data[2][1]}')

print('-' * 100)
# 需求：实现列表的遍历
# 定义一个总公司的销售额
company_sum = 0
for i in range(len(list_data)):     # [0, 1, 2]
    # list_data[i]    # 取出内部的小整体

    # 定义一个小组的统计变量
    group_sum = 0
    for j in range(len(list_data[i])):
        # print(f'list_data[i][j] = {list_data[i][j]}' )
        value = list_data[i][j]
        group_sum += value
    print(f'第{i + 1}小组的销售额是：{group_sum}')
    print('-' * 100)

    company_sum += group_sum
print(f'公司总的销售额是：{company_sum}')

print('-' * 100)


company_sum = 0
for group in list_data:
    # print(group)
    group_sum = 0
    for value in group:
        # print(value)
        group_sum += value
    company_sum += group_sum
    print(f'group_sum = {group_sum}')
print(f'company_sum = {company_sum}')