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
# 列表中的删除
# 1.remove(元素)
names.remove('王五')
print(names)
# 2.1 pop(下标)
names.pop(0)
print(names)
# 2.2 pop()     默认删除尾部元素
names.pop()
print(names)
# 3.clear() 清空列表 => 该列表成为一个空列表
names.clear()
print(names)

names.extend(['刘德华', '张学友', '黎明', '郭富城'])
print(names)

# del 列表名  Python语言的内置方法，不是列表方法
del names   # 将整个names列表从内存中删除了，意味着这个names列表不能再使用了

# print(names)    # 报错 NameError: name 'names' is not defined 名称未定义
