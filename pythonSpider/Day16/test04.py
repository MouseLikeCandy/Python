# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 18:56
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
split()     切割扩展
'''
if __name__ == '__main__':
    regEx = '#+'
    str = 'boxing#####basketball#####football####fitness####ILOVEYOU######爱我中华'
    regEx = r'\d+'
    str = 'boxing1234556basketball94389football8888fitness9999ILOVEYOU37827392爱我中华'

    words = re.split(regEx, str)
    for word in words:
        print(word)

