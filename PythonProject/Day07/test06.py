# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 21:00
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 字典dictionary
# 映射关系  key -> value    根据key(键)查找value(值), 字典元素是成对出现的Item,简称键值对(一个键值对是一个元素) 
# 格式：{key1: value1, key2: value2, key3: value3,... }    # 不要在key的后面加空格
# 字典一般不使用下标取值
'''
scores = {'张三': 100, '李四': 99, '王五': 88, '赵六': 66}
# 这个字典中有多少个元素/键值对？

# KeyError: 0
# print(scores[0])

# item  翻译为  元素/键值对   依据上下文
# keys 键集  values 值集   items 键值对集
print(f'keys = {scores.keys()}')
print(f'values = {scores.values()}')
print(f'items = {scores.items()}')
# 遍历
# 方式一: 键集keys
keys = scores.keys()
for key in keys:
    print(f'key = {key}')
# 方式二: 值集values
values = scores.values()
for value in values:
    print(f'value = {value}')
# 方式三: 键值对集items
items = scores.items()
for item in items:
    print(f'item = {item}')

# 由于 item 对象是一个元素, 包含了两个数据, 我们可以在遍历时, 直接定义两个变量.
# 元组特点: 自动完成数据的解包/拆解元组中的数据
for key, value in items:
    print(f'key = {key}, value = {value}')


# 字典如何操作？
# 1.使用key来找对应的value
# 2.使用items来找到每一个键值对

# 需求： 查看张三的考试成绩
print(f'scores["张三"] = {scores["张三"]}')

# 需求： 查看马八的考试成绩
# KeyError: '马八'
# print(f'scores["马八"] = {scores["马八"]}')

# 查询中如果字典中的key不存在，程序就会报错。

print('-' * 100)

key = input('亲，请输入要查询成绩的学生姓名：')
# 判断
# if key in scores.keys():
if key in scores:       # 如果在判断中，直接书写字典名称，其实本质就是调用了字典对象的keys()
    # key存在
    print(f'scores[{key}] = {scores[key]}')
else:
    # key不存在
    print(f'数据库中不存在该学生。')

print('-' * 100)
for item in scores:     # 如果在循环中，直接书写字典名称，其实本质就是调用了字典对象的keys()
    print(item)

print('-' * 100)
for item in scores.items():
    print(item)

print('-' * 100)
for key, value in scores.items():
    print(key, value)

# 在字典中,key是唯一性的,value是可以重复的.
# 如果key相同,新值就会覆盖旧值.
# 如果key不存在,此操作就是'新增',如果key已经存在,此操作就是'修改'.
# 只能通过key来找value，不能通过value来找key
