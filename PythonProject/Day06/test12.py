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
names = ['张三', '李四', '王五', '赵六', '田七']
print(names)

# 列表的主要操作方法：增删改查
# 增删改查 CRUD
# crud是指在做计算处理时的增加(Create)、检索(Retrieve)、更新(Update)和删除(Delete)几个单词的首字母简写。
# crud主要被用在描述软件系统中数据库或者持久层的基本操作功能。
# 列表元素的修改通过下标实现
# 将‘王五’更新为‘马八’
names[2] = '马八'
print(names)

name = names[2]
print(name)
