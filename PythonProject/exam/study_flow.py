# 比较运算符
a = 10
b = 17
print(a > b)
print(a <= b)

c = 'abc'
d = 'bbc'
print(c < d)
print(c != d)
# ord方法
for c_content in c:
    print(ord(c_content))
for d_content in d:
    print(ord(d_content))

e = 123 
f = '99'   

i = 0
while i < 3:
    print(str(e)[i], end='\t')
    i +=1
print()

j = 0
while j < 2:
    print(f[j], end='\t')
    j +=1 
print()

#print(e > f)
print(str(e) > f)



# 逻辑运算符
a = 10
b = 17
c = 18
d = 20
print(a < b and b < c)
print(a < b or c < d)
print(not a > b)


# 判断语句
if  a != b:
    print('!=')
else:
    print('==')


if c >= d or a > b:
    print('or')
elif b > c:
    print('b > c')
elif c < a:
    print('c < a')
else:
    print('no i want')



a = 1
for i in range(0, 101):
    if a[i] == a(i - 1) + a(i - 2):
        print(a(i))