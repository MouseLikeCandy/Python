# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/23 21:14
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    函数（内存执行过程）
    源数据 => 返回值
    
    用于完成指定的一段程序功能：①求和  ②根据key从映射表中取值的功能
    
    1.源数据 / 形式参数（实际参数） 实现该功能需要的数据
    2.返回值（编程中一段功能可能没有返回值）
    
    格式：
    定义函数：
        def 函数名称（参数1，参数2， ...）
            函数执行体1...
            函数执行体2...
            函数执行体3...
            return 值
    调用函数：
        变量 = 函数名称(参数1，参数2，...)
'''


# 如果一个函数没有返回值，在函数末尾也会自动存在一个return关键字
# 如果一个函数没有返回值，末尾也自动有return,那返回了什么？ None 空对象 / 空值
# Python中, 不能对NOne对象进行任何操作

# return关键字可以在函数体的任意位置出现，一旦函数执行到return关键字，函数就会立即结束。


# 定义一个求和的函数, 如果这个函数不能调用，就永远不会执行。
# 如果调用多次，就会被执行多次。
# definition 定义
# 定义函数
def get_sum(sum1, sum2):
    sum = sum1 + sum2
    return sum


# 调用函数
# 变量 = 函数名称(参数1，参数2，...)
result = get_sum(10, 20)
print(f'result = {result}')

result = get_sum(100, 200)
print(f'result = {result}')

print('程序继续向下执行...')
