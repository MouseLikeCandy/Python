# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 21:01
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re  # python语言直接提供的'正则模块'
'''
正则表达式

# 字符串数据类型在程序开发中是最常见的数据类型.
# 编程中有专门的的一个语法, 用于处理字符串, 主要就是对字符串进行'匹配. 切割. 替换. 获取'四大能力 -> 正则表达式
'''


def vertifyQQNumber2(qq):
    # 正则: 一些特殊符号具有特殊的含义
    regEx = '^[1-9][0-9]{4,11}$'  # regular expression
    # 第一位[1-9]
    # 第二位[0-9], {4,11}表示重复4-11次
    # matcher 正则返回的匹配器对象, 如果没有匹配到内容就是None对象
    matcher = isinstance(regEx, str) and re.match(regEx, qq)  # 说明: match()完毕后会返回一个'正则对象'
    return True if matcher else False


# 定义一个函数用于验证QQ号码是否合法
def vertifyQQNumber(qq):
    if not isinstance(qq, str):
        return False

    # 1. 第一位不能是0
    if qq[0] == '0':
        print('qq号码第一位不能为0')
        return False
    # 2. QQ号码在5~12为位之间
    elif len(qq) < 5 or len(qq) > 12:
        print('qq号码在5 ~ 12位之间(包含)')
        return False
    # 3. QQ号码都是由数字组成的
    else:
        return qq.isdecimal()  # 十进制


# 测试
if __name__ == '__main__':
    qq = input('亲, 请输入QQ号码:')
    # 调用函数
    result = vertifyQQNumber(qq)
    print(f'result = {result}')

    result2 = vertifyQQNumber2(qq)
    print(f'result2 = {result2}')
