# dict 字典  键值对
d1 = dict()
d2 = {'a': 1, 'b': 2, 'c': 3}
print(d1)
print(d2)
print(d2['a'])
d2['a'] = 6
print(d2['a'])

# del  clear
del d2['a']
# print(d2['a'])
print(d2)

d2.clear()
print(d2)

# clear  vs  {}
d3 = {'a': 123, 'b': 456, 'c': 789}
print(f'id(d3) = {id(d3)}')
d3.clear()
print(id(d3))

d4 = {'a': 123, 'b': 456, 'c': 789}
print(f'id(d4) = {id(d4)}')
d4 = {}
print(id(d4))

# 取键
d = {'a': 123, 'b': 456, 'c': 789}
for i in d:
    print(i)
# 取键和值
for k, v in d.items():
    print(k, v)
# 取值
for v in d.values():
    print(v)
# 取键
for k in d.keys():
    print(k)

# 将具有相同值的键整理出来
d = {'a': 1, 'b': 1, 'c': 3, 'd': 4, 'e': 3, 'f': 1, 'g': 4}
new_d = {}
for k, v in d.items():
    new_d.setdefault(v, [])
    print(f'by setdefault new_d = {new_d}')
    new_d[v].append(k)
    print(f'by append change list new_d = {new_d}')
print('-' * 100)
print(new_d)
# setdefault函数会在字典中查找是否存在当前键, 如果存在则返回所对应的值, 不存在则在字典中创建该键值对
# 一开始new_d字典中并没有键值对, 所以会生成一个键为1,值为[]的键值对
# setdefault的返回值: 如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
# 从表面上理解就是设置默认的键值对,设置不成功说明已经存在


import collections

d = collections.OrderedDict()
print(type(d))
print(isinstance(d, dict))
