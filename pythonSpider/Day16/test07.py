# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 18:43
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
re模块的三大搜索函数:
match()     单值匹配
search()    单值匹配
findall()   全文查找, 返回 字符串 列表
finditer()  全文查找, 返回 match object 列表
'''


if __name__ == '__main__':
    regEx = r'[1-9]\d{5}'
    str = 'BJ100100 SH100200 GZ100300 SZ100400'

    re.match(regEx, str)
    re.search(regEx, str)
    # finditer()返回的是一个列表, 但是列表中存储的是 match object 对象.
    zip_code_matchers = re.finditer(regEx, str)     # <re.Match object; span=(2, 8), match='100100'>
    for code_mather in zip_code_matchers:
        print(code_mather)
        print(code_mather.group())

