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
findall()   全文查找, 返回列表

split()     切割
'''


if __name__ == '__main__':
    regEx = r'[1-9]\d{5}'
    str = 'BJ100100 SH100200 GZ100300 SZ100400'

    zip_codes = re.split(regEx, str)
    for code in zip_codes:
        print(code)

    regEx = r' +'   # 表示以1个或多个空格作为切割符
    str = 'BJ100100 SH100200  GZ100300    SZ100400'

    zip_codes = re.split(regEx, str)
    for code in zip_codes:
        print(code)

