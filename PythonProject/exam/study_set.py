# set 集合  无序  无重复
s = {2, 4, 5}
print(s)

# 增加元素
s.add(66)
print(s)

s.update({5, 6, 6, 7, 8})
print(s)

# 删除
s.remove(66)
# s.remove(67)
print(s)
s.discard(67)
s.discard(7)
print(s)

print('-' * 100)
# 去重
l1 = [1, 2, 4, 5, 5, 5, 3, 2, 5, 7, 7, 7, 8]
print(l1)
s = set(l1)
print(s)
l2 = list(s)
print(l2)



# 集合运算
# &交集    intersection
s1 = {1, 3, 4, 5, 7}
s2 = {2, 5, 67, 6, 7, 9}
print(f's1 = {s1}')
print(f's2 = {s2}')
s3 = s1 & s2
print(f's1 & s2 = {s3}')

s3 = s1.intersection(s2)
print(f's1.intersection(s2) = {s3}')

# - 差集    difference
s4 = s1 - s2
print(f's1 - s2 = {s4}')
s4 = s2 - s1
print(s4)

s4 = s1.difference(s2)
print(f's1.difference(s2) = {s4}')

# | 并集  union
s5 = s1 | s2
print(f's1 | s2 = {s5}')
s5 = s1.union(s2)
print(f's1.union(s2) = {s5}')
# ^ 对称差集
s6 = s1 ^ s2
print(f's1 ^ s2 = {s6}')
s6 = s1.symmetric_difference(s2)
print(f's1.symmetric_difference(s2) = {s6}')


