# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 20:25
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
    enumerate迭代器, 如果传入一个列表，则将列表中得到每一个元素与下标组合
'''

names = ['张三', '李四', '王五', '赵六', '田七', '马八']
for name in enumerate(names):
    # (0, '张三')元组类型，元祖中的元素是不可改变的
    print(name)

print('*' * 100)

# 元素中有两个元素， 因此我们我可以在for循环中定义两个变量名
for index, name in enumerate(names):
    print(index, name)