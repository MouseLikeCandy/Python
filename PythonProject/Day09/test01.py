# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 20:04
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 自定义函数, 返回多个结果.
# 定义一个函数, 返回奇数列表和偶数列表
'''


def get_odd_and_even(number_list):
    even_list = []
    odd_list = []
    # 遍历传入的数值列表
    for number in number_list:
        # 判断当前遍历的数值是奇数还是偶数
        if number % 2 == 0:
            # 偶数
            even_list.append(number)
        else:
            # 奇数
            odd_list.append(number)
    return odd_list, even_list


# 定义一个列表
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 调用函数
result = get_odd_and_even(num_list)

print(f'奇数列表:{result[0]}')
print(f'偶数列表:{result[1]}')

# 如果在函数中返回了多个结果,其真正返回结果类型为'元组'类型
