# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 9:51
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
format格式化
'''
name = '张三'
age = 18
money = 99.99

if __name__ == '__main__':
    print(f'大家好, 我叫{name}, 今年{age}岁, 没骗你, 我真的只有{age}岁.我有{money}块.我真的叫{name}.')
    print('大家好, 我叫{0}, 今年{1}岁, 没骗你, 我真的只有{2}岁.我有{3}块.我真的叫{4}.'.format(name, age, age, money, name))
    print('大家好, 我叫{0}, 今年{1}岁, 没骗你, 我真的只有{1}岁.我有{2}块.我真的叫{0}.'.format(name, age, money))
    print('大家好, 我叫%s, 今年%d岁, 没骗你, 我真的只有%d岁.我有%.2f块.我真的叫%s.' % (name, age, age, money, name))