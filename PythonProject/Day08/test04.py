# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/23 21:14
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    函数的定义/调用/执行
    
    函数（内存执行过程）  
    内存中的栈区（stack）: 执行函数和方法的内存空间
    特点: 先进后出
        进入: 入栈push
        出来: 弹栈pop
        
    如果程序中的代码没有写在自定义函数中,那么这些代码默认全部位于'主函数'中,主函数(main)是程序执行的入口.
    程序执行:内存中开辟空间
        main函数入栈
            调用函数入栈
                return 30
            调用函数弹栈
            调用函数入栈
                return 300
            调用函数弹栈
        main函数弹栈,程序结束
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
