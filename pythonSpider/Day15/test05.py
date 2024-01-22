# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/15 6:42
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
匹配模式
re.I    忽略大小写
re.M    ^   将给定字符串的每行当做匹配开始
re.S    .   匹配所有字符, 包括换行.(默认不包括换行)
'''
import re


if __name__ == '__main__':
    regEx = 'hello.*Demo'
    with open('test.txt', mode='rt', encoding='utf-8') as f:
        str = f.read()      # str数据具有换行的特性

    print(str)

    matcher = re.match(regEx, str)
    print(matcher)

    matcher = re.match(regEx, str, re.S)
    print(matcher)

    print('-' * 100)
    regEx = '^love.*'
    with open('test_M.txt', mode='rt', encoding='utf-8') as f:
        str = f.read()

    matcher = re.match(regEx, str, re.M)        # 让每一行都按照regEx正则的规则进行匹配
    print(matcher)

    # findall() 查找
    result_set = re.findall(regEx, str, re.M)   # 让每一行都按照regEx正则的规则进行匹配
    for result in result_set:
        print(result)

    print('-' * 100)
    regEx = 'ABc'
    str = 'abc123abC'
    matcher = re.match(regEx, str, re.I)
    print(matcher)
    print(matcher.group())



