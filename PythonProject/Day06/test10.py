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
'''
names = ['张三', '李四', '王五', '赵六', '田七']
print(names)
# 在后面向列表中添加元素
# 1.append(元素)  拼接
names.append('马八')
print(names)
# 2.insert(下标, 元素) 插入
names.insert(2, '小二')   # 指定下标位置的插入
print(names)
# 3.extend()
names.extend(['刘德华', '张学友', '黎明', '郭富城'])
names.extend(['张三'])
print(names)
