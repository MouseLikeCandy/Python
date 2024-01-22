# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 19:51
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re

if __name__ == '__main__':
    # 分组    在第0组的基础上进行分组
    regEx = r'.*(¥\d+).*(¥\d+)'
    str = 'this book is ¥10, that book is ¥20.'

    matcher = re.search(regEx, str)
    if matcher:
        print(matcher.group())  # 匹配到的所有内容默认存储在第0组
        print(matcher.group(0))
        print(matcher.group(1))
        print(matcher.group(2))
    else:
        print('没有查找到数据.')



