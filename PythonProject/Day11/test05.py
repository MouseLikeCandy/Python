# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/9 6:21
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
isinstance 是否为某一具体的实例对象
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
作用: 实现具体对象的具体类型判断
'''

if __name__ == '__main__':
    num = '10'
    r1 = isinstance(num, int)
    print(r1)

    num_list = [10, 20, 30, 40, 50]
    r2 = isinstance(num_list, list)
    print(r2)

    name_dict = {'name': '张三', 'age': 20}
    r3 = isinstance(name_dict, dict)
    print(r3)