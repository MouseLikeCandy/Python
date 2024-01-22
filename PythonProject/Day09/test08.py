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
    
    main函数, 程序的入口. 
    如果不写, 会被自动包装到主函数中   
'''


def function_one():
    global n
    print(f'function_one n = {n}')  # NameError: name 'n' is not defined # 名称错误: n 名称没有被定义 # 声明在定义之前

    n = 100  # 修改全局变量n的数值
    print(f'function_one n = {n}')


def function_two():
    n = 20


def function_three():
    pass


# 书写主函数名称
if __name__ == '__main__':
    n = 999
    # 调用函数
    function_one()
    # 思考: 此处能否调用function_one中的n变量
    # print(f'n = {n}')   # Unresolved reference 'n'  无法解析 n 这个引用

    print(f'n = {n}')

    # 代码没有写在自定义函数中,那么这些函数就相当于写在了主函数中

# 多个py文件相交互, 互相使用数据, 需要定义main函数, 否则出现错误
