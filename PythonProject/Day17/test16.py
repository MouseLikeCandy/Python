# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 21:48
@Auth ： 异世の阿银
@File ：test16.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
访问数据
'''

from Day17.model import Student
import shelve

if __name__ == '__main__':
    # 1. 打开shelve
    stus = shelve.open('stus')
    # 2. 访问数据
    for key, value in stus.items():
        print(key, value)

    # 修改
    stu = Student('1001', '小三三', 20, 100)
    stus['1001'] = stu

    # 添加
    stus['1001'] = Student('1006', '赵六', 33, 101)


    # 删除
    stus.pop('1002')

    # 3. 关闭shelve
    stus.close()