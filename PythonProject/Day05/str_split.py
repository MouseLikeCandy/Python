# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 21:34
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
# 知道 ：
# 字符串已经拥有了很多行为： str类型定义完毕的，可直接使用
# 1. 根据下标查找字符。
# 2. 根据字符查找下标。index() rindex() find() rfind()
# 3. 可以实现字符/字符串的大小写转换 upper() lower()
# 4. 字符串还可以根据制定字符串实现分割，split()
# 5. 判断字符串是否为数字字符串 isdecimal() isnumric()
# 6. 字符串内容可以实现替换 replace()
# 7. 字符串数据的合并 join()
'''


# 定义一个字符串
language = 'Python|C|C#|java|HTML|C++|PHP|JavaScript'

# split(切割符) =>返回一个数据列表
program_list = language.split('|') # 列表数据类型
print(f'program_list = {program_list}')

# program_list列表有8个元素，0~7的下标
# python的内置方法： len（整体变量） -》返回整体变量的长度
print(f'len(program_list) = {len(program_list)}')

for i in range(len(program_list)):
    # 可以通过下标，从整体中取值
    print(f'{program_list[i]}')

# Python 这个字符串中的P

# 1. 第一个步骤是根据列表的下标，取出对应的字符串
word = program_list[0]
print(f'word = {word}')

# 2. 第二个步骤是根据字符串的下标，取出对应的字符
subword = word[0]
print(f'subword = {subword}')

