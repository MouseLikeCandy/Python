# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 20:50
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 元组
'''
    CRUD 增删改查
    
    不可变序列: 字符串/元组(没有增删改的操作)
    可变序列: 列表/字典(可以增删改操作,对象地址不发生更改)
    
    元组的特点：tuple
    不可变序列, 元组不能对元组中的元素执行增删改, 只能查询
    用途: 数据的传输, 不能被修改
'''

# 数据：（学号，姓名， 年龄， 成绩）
stu1 = ('1001', '张三', 20, 88)
stu2 = ('1002', '张三', 22, 65)
stu3 = ('1003', '张三', 24, 99)
print(stu1)
print(stu2)
print(stu3)

# 尝试进行'增删改'操作
# TypeError: 'tuple' object does not support item assignment
# 类型错误：元组对象不支持元素的重新赋值
# stu1[0] = '1010'
# print(stu1)

# 主要使用场景：'数据传递'。
# 数据传递：
# 1. 函数/方法 的参数类型上传递数据。
# 2. 执行函数/方法后，在返回结果上实现数据的传递

# 注意： 元组类型中，如果有且仅有一个元素，定义完毕元素后，一定要跟一个逗号
# num_tuple = (10)
num_tuple = (10,)
print(num_tuple, type(num_tuple))