# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:47
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 复合赋值运算符  += -= *=  /=  //=  %=   **=
# 特点：如果一个变量需要自身的基础上实现数据的更改/变量，此时，就可以使用复合运算符

num1 = 10
# 说明：如果一个变量需要在自身的基础上实现运算，此时，我们就可以使用 复合赋值运算符
# num1 = num1 + 1  # 将num中的数值取出来,实现+1的运算，将结果再保存到num中
num1 += 1
print(f'num1 = {num1}')


