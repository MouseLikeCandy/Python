# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 20:50
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 三目运算符： 是 if else 双分支结构的简化写法
# 语法格式：    变量  =  结果1  if bool条件表达式 else 结果2
# 条件成立返回左边值，不成立返回右边数值
# 后面有很多逻辑处理就不能用三目运算实现

# 判断3个整型数值中的最大值

# 1.定义变量，接收用户的输入
num1 = int(input('亲，请输入第一个整型数值：'))
num2 = int(input('亲，请输入第二个整型数值：'))
num3 = int(input('亲，请输入第三个整型数值：'))

# 2.三目运算判断
# 两两判断，获取较大的数值
second_max = num1 if num1 > num2 else num2
# 两两判断，获取最大的数值
max = second_max if second_max > num3 else num3
print(f'max = {max}')
