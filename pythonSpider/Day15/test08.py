# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/15 7:11
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
match() 与 search()
为了匹配方便, 能用search不用match
'''
import re

if __name__ == '__main__':
    regEx = 'Hello.*Demo'
    str = 'Hello Wolrd! This is a regEx Demo!'

    # match() 和 search() 都返回matcher (match object) 对象
    matcher = re.match(regEx, str)
    if matcher:
        print(matcher.group())
    else:
        print('没右匹配到!')

    # match()方法有局限性, 要求源数据必须指定规则开头.
    str = 'Extra string! Hello Wolrd! This is a regEx Demo! Extra string! '
    matcher = re.match(regEx, str)
    if matcher:
        print(matcher.group())
    else:
        print('没右匹配到!')

    # search() 全文档搜索, 不要求源数据必须指定规则开头.
    str = 'Extra string! Hello World! This is a regEx Demo! Extra string! '
    matcher = re.search(regEx, str)
    if matcher:
        print(matcher.group())
    else:
        print('没右匹配到!')