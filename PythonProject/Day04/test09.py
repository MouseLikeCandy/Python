# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 19:12
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 需求： 倒直角三角形
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

# 1.外层循环
for i in range(5):
    # 2. 内层循环
    for j in range(5-i):
        print('*', end=' ')

    print()

print('*' * 100 )

for i in range(-5):   # 从零开始，到-5结束，所以不循环
    print()