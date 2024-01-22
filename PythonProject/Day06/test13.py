# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 21:19
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 列表的特点
# 元素有序（放入顺序）存取有序
'''
    列表的特点
    1.元素存取有序
    2.元素有索引
    3.元素可重复
    4.列表的长度是动态可扩展的
'''
num_list = [55, 45, 12, 44, 88, 77, 22, 11, 33, 99, 66]
print(num_list)

# 列表中元素的排序  sort()  正向排序
num_list.sort()
print(num_list)
# 2.逆向排序    sort(reverse=True)
num_list.sort(reverse=True)     # 翻转
print(num_list)

