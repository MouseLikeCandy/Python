# tuple 元组  有序,不可修改
t1 = tuple([1, 2, 3])  # tuple方法, 参数list
t2 = (4, 5, 6)
print(t1)
print(t2)

# t1[0] = 8

print(id(t1))
print(id(t2))
t1 = t1 + t2
print(t1)
print(id(t1))

# 通过下标或者切片的方式获取元组的值
print(t1[3])
print(t1[1:5])

# 修改了元组中的值?
# t[3]指向一个列表,并未发生改变
t = (1, 2, 4, [3, 4, 6])
print(t)
t[3][0] = 8
print(t)



