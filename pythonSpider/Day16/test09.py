# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 21:09
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
re.compile 将正则字符串编译成正则表达式对象, 以便于复用该匹配模式.
编译为Pattern模式对象
re.search() => regex = re.compile() + regex.search()
re.findall() => regex = re.compile() + regex.findall()
...
'''
if __name__ == '__main__':
    # 需求: 从字符串中查找有3个字符的单词
    str = 'good good study, day day up. 0~ yes!'
    regEx = r'\b[A-Za-z]{3}\b'
    # 1. 将正则字符串编译为一个'正则对象'
    pattern = re.compile(regEx)

    # 2. 使用正则对象调用正则的对应方法
    words = pattern.findall(str)

    # 3. 查看数据
    for word in words:
        print(word)

    print('-' * 100)

    str2 = 'Jack loves May, May loves Tom, Tom loves Lily. How pity it is.'
    words = pattern.findall(str2)
    for word in words:
        print(word)