# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 20:55
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
    变量的作用范围: 作用域
    自定义函数中的变量的作用域仅在函数中有效
'''

def function_one():
    n = 100
    print(f'function_one n = {n}')


# 调用函数
function_one()
# 思考: 此处能否调用function_one中的n变量
# print(f'n = {n}')   # Unresolved reference 'n'  无法解析 n 这个引用



n = 999
print(f'n = {n}')

# 代码没有写在自定义函数中,那么这些函数就相当于写在了主函数中

