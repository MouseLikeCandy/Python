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


# 根据字符/子串查找其对应的下标位置。
str = 'hello, Python'

index = str.index('o')
print(f'index = {index}')

rindex = str.rindex('o')
print(f'rindex = {rindex}')

find = str.find('o')
print(f'find = {find}')

rfind = str.rfind('o')
print(f'rfind = {rfind}')

# 如果查询一个不存在的字符
# index报错 ValueError: substring not found
# x_index = str.index('x')
# print(f'x_index = {x_index}')
# find不报错，返回-1
x_find = str.find('x')
print(f'x_find = {x_find}')