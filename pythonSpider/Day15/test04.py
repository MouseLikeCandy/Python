# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/15 6:29
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re


if __name__ == '__main__':
    # 定义参数
    regEx = 'Hello.*Demo'
    str = 'Hello world! 1234 this is a 6789 regEx 0123 Demo'
    # 匹配器对象
    matcher = re.match(regEx, str)
    print(f'matcher = {matcher}')
    if matcher:
        result = matcher.group()
        print(matcher.group())
        print(matcher.span())
        print(f'matcher.group(0) = {matcher.group(0)}')     # 匹配到的所有结果统称为第0组, 第0组是整个匹配的整体, 默认就是第0组.
    else:
        print('没有匹配到任何结果.')

    # 需求: 取数据
    # .* 0个或多个  越多越好. (贪婪模式)
    # .*? 能少就少         (非贪婪模式)
    regEx = r'Hello.*(\d+).*(\d+).*(\d+).*Demo'
    str = 'Hello world! 1234 this is a 6789 regEx 0123 Demo'
    matcher = re.match(regEx, str)
    print(f'matcher.group(0) = {matcher.group(0)}')
    print(f'matcher.group(1) = {matcher.group(1)}')
    print(f'matcher.group(2) = {matcher.group(2)}')
    print(f'matcher.group(3) = {matcher.group(3)}')

    regEx = r'Hello.*?(\d+).*?(\d+).*?(\d+).*?Demo'
    str = 'Hello world! 1234 this is a 6789 regEx 0123 Demo'
    matcher = re.match(regEx, str)
    print(f'matcher.group(0) = {matcher.group(0)}')
    print(f'matcher.group(1) = {matcher.group(1)}')
    print(f'matcher.group(2) = {matcher.group(2)}')
    print(f'matcher.group(3) = {matcher.group(3)}')