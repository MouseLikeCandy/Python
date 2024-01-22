# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 18:18
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# range()函数  =>范围
# 含义： 在编程中，range()函数可以帮助我们生成指定范围内的数值序列

'''
    range(start, stop, step)
    1. start 开始 
    2. stop 结束（不包含该结束的数值）=》计算机默认是从零开始的。
    3. step 步长（每次增长多少数值）可以不写，默认每次增长1个数值。
    
    说明：如果我们仅仅是需要循环的一个次数，并不需要指定范围的数值，会直接书写一个变量，那就是stop
    
'''

# 1. 整型数值 1~10 之间的范围数值
# r = range(1, 11, 1)
# print(r) # 返回range对象

i = 1
while i < 11:
    print(i, end='\t')
    i += 1

print()

# 使用场景：for 循环变量 in range(): 再循环内部就可以使用循环变量了
for i in range(1, 11, 1):
    print(i, end='\t')

print()

# 注意1 ：range(数值) => stop 这个数值
for i in range(10):   # stop = 10   range(0, 10, 1)
    print(i, end='\t')

print()

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print()

i = 10
while i < 101:
    print(i, end='\t')
    i += 10

print()

for i in range(10, 101, 10):
    print(i, end='\t')

print()

# 小结1：while循环一般在循环次数未知的情况下使用，大多数情况下会和break关键字连用。
# 小结2：for + range()一般在循环次数确定的情况下使用，range()可以帮助我们程序生成一个循环的指定范围。


# [101, 91, 81, 71, 61, 51, 41, 31, 21, 11, 1]
for i in range(101, 0, -10):
    print(i, end='\t')

print()

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] = > 列表生成器
for i in range(1, 11, 1):
    print(i ** 2, end='\t')
    print(i * i, end='\t')
