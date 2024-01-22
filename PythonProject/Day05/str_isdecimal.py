# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/6 5:57
@Auth ： 异世の阿银
@File ：str_isdecimal.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
# 判断支付密码是否合法
# 需求： 密码只能由‘数字字符串’组成
'''

# 1.定义一个变量，接收用户输入
password = input('亲，请输入你的密码：')

# 2.判断 password 字符串是否由数字组成
# 字符串是一个'对象类型'。如果是对象就一定可以.() 这是对象的方法
# 思考：字符串有没有提供这个一个用于判断数据内容是否为数字的方法？
# decimal 十进制的数字
# Return True if the string is a decimal string, False otherwise.
# 返回True,如果指定字符串是一个十进制的字符串，否则返回False
valid = password.isdecimal()
# digit 数字
# Return True if the string is a digit string, False otherwise.
valid = password.isdigit()

if valid:
    print('密码不合法。')
# 查看结果
else:
    print('密码合法。')