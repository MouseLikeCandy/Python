# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 21:04
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 字符串拼接/合并
# 定义一个字符串
language = 'Python|C|C#|java|HTML|C++|PHP|JavaScript'
# 切割   将字符串切割成列表
program_list = language.split('|')
print(program_list)

# 合并    将列表合并成字符串
result = '='.join(program_list)     # 用‘符号’合并字符串
print(result)

result = '=》'.join(program_list)     # 用‘符号’合并字符串
print(result)
