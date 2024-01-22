#  容器 list列表 有序
#  append
list1 = list()
list1.append(1)
list1.append('abc')
list1.append([2, 3, 4])
print(list1)

a = [1, 2, 3]
a.append(a)
print(a[3])
print(a[3][3])
print(a[3][3][3])

#  extend
b = [4, 5, 7]
b.extend([3, 2, 1])
print(b)
# 下标取值
for i in b:
    print(i, end='\t')
#    i += 1
print()
for j in range(len(b)):
    print(b[j], end='\t')
    j += 1
print()
# 切片取值
print(b[1:4])
# 修改下标所对应的值
b[3] = 66
print(b)
# 删除下标所对应的值
del b[2]
print(b)
# 删除列表中某个值的第一个匹配项
b.append('asdf')
b.extend([66])
b.append('asdf')
print(b)
b.remove('asdf')
print(b)

# 排序sort
b.remove('asdf')
b.sort()
print(b)

b.sort(reverse=True)
print(b)

list2 = []
for i in b:
    if i % 2 == 0:
        list2.append(i)
print(list2)