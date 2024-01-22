# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:35
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 模拟用户的输入（姓名，年龄，性别）然后输出用户的所有信息
# input(提示用户的显示信息）
# input 是一个输入函数，需要用户在控制台中输入结果，程序才会继续向下执行，如果不输入，程序在此处'死等'
name = input('亲，请输入您的姓名：')
age = input('亲，请输入您的年龄：')
gender = input('亲，请输入您的性别：')
print(f'大家好，我叫{name},今年{age}岁，性别{gender}')


# input()函数
print(f'程序来到了这里1...')
# 1.input()输入函数可以阻塞程序继续向下执行。
# 2.input()输入函数在等待用户通过键盘向程序输入内容。
# 3.input()输入函数会将用户在控制台输入的内容返回给我们，我们需要使用变量来接收。
# 4.input()输入函数无论用户在控制台输入的啥数据，结果都是字符串类型。
result = input('兄弟，今天的天气怎么样？')
print(f'type(result) = {type(result)}, result = {result}')
print(f'程序来到了这里2...')

# 需求：通过键盘输入数据，实现算术运算符
# 从控制台输入两个整型数值输入，然后实现加法运算，输出运算结果
# 注意： input函数返回的结果为str类型
# 复制： Ctrl + D

num1 = input('亲，请输入第一个整型数值：')
num2 = input('亲，请输入第二个整型数值：')

print(f'type(num1) = {type(num1)}, type(num2) = {type(num2)}')
# 运算summary
sum = num1 + num2
print(f'sum = {sum}')
