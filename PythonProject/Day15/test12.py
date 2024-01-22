# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 15:07
@Auth ： 异世の阿银
@File ：test12.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
转义字符

raw string 原生字符串.
作用: 将 \ 转移字符含义去除掉
'''

print('hello world')

print('hello\nworld')

# \ 转义字符的含义     去除转移含义 \\
print('E:\PythonProject\Day15\test12.py')
print('E:\\PythonProject\\Day15\\test12.py')
# \ 转换为 /
print('E:/PythonProject/Day15/test12.py')

# raw string
print(r'E:\PythonProject\Day15\test12.py')