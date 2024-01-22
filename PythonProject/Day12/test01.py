# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 20:02
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 内置函数 : isinstance(变量, 类型)  is开头这样的方法返回的结果是bool类型的结果  instance / objec 对象

'''

if __name__ == '__main__':
    num = 10
    result = isinstance(num, int)
    print(f'result = {result}')

    num_list = [10, 20, 30, 40, 50]
    result = isinstance(num_list, list)
    print(f'result = {result}')

    name_dict = {'name': '张三', 'age': 18}
    result = isinstance(name_dict, dict)
    print(f'result = {result}')
