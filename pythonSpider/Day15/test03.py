# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/15 6:22
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re

'''
带转义的使用原生字符串

正则的匹配 match()
'''


if __name__ == '__main__':
    # 定义参数
    regEx = 'Python'
    str = 'Python and java'
    # 匹配器对象
    matcher = re.match(regEx, str)    # match()返回一个Matcher匹配器对象
    print(f'matcher = {matcher}')
    # matcher要么有结果, 要么就是一个None对象
    if matcher:
        # 取出matcher对象中的匹配结果
        result = matcher.group()    # group() 组
        print(result)
    else:
        print('没有匹配到任何结果.')

