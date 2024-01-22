# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 6:43
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 五行五列的正方形
# 1.外层循环（行）
for i in range(5):
    # 2.内层循环（列）
    for j in range(5):
        print('*', end='')
    # 内层循环完毕后需要换行
    print()

