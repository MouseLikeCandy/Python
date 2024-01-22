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
    
    主函数中定义的变量 - 全局变量    可以在所有自定义函数中使用
    global 关键字的作用:
    将局部变量改为全局变量, 在程序运行期间只有一份    
'''


def function_one():
    global n
    print(f'function_one n = {n}')  # NameError: name 'n' is not defined # 名称错误: n 名称没有被定义 # 声明在定义之前

    n = 100  # 修改全局变量n的数值
    print(f'function_one n = {n}')


#
# def function_one():
#     n = 100
#     print(f'function_one n = {n}')
#     # 声明n 变量为全局参数
#     # SyntaxError: name 'n' is used prior to global declaration
#     # 语法错误: n 变量名称在全局声明之前已经被使用过了
#     global n
#     print(f'function_one n = {n}')

# 调用函数
function_one()
# 思考: 此处能否调用function_one中的n变量
# print(f'n = {n}')   # Unresolved reference 'n'  无法解析 n 这个引用


n = 999
print(f'n = {n}')

# 代码没有写在自定义函数中,那么这些函数就相当于写在了主函数中
