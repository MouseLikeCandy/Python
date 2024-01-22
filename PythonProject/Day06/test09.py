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
'''
names = ['张三', '李四', '王五', '赵六', '田七']

# 从names中取出‘王五’
name = names[2]
print(name)

# 列表也是“对象数据类型”
# 生活中如何理解：对象（女朋友）->行为（做饭，打扫卫生，按摩，洗衣服，生孩子。。。）
# 编程中对象行为：列表对象 -> 行为 index(), append(), insert(), [start:stop:step], in, not in, extend(), pop(), remove()...

# 查询‘王五’在列表中的下标
index = names.index('王五')
print(f'index = {index}')

# 查询列表中不存在的元素
# index = names.index('嘛吧')
# print(f'index = {index}')

# 元素在列表中是否存在的判断方法
result = '马八' in names
print(f'result = {result}')

name = input('亲，请输入要查找的元素：')
if name in names:
    index = names.index(name)
    print(f'index = {index}')
else:
    print(f'列表中不存在该元素')