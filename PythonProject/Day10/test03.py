# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/27 21:15
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
    集合的数学操作:
    交集
    并集
    差集
'''
if __name__ == '__main__':

    set1 = {10, 20, 30, 40}
    set2 = {20, 30, 40, 50, 60}

    # 交集 intersection -> & (与)
    r1 = set1.intersection(set2)
    print(f'r1 = {r1}')

    r1 = set1 & set2
    print(f'r1 = {r1}')

    # 并集 union -> | (或)
    r2 = set1.union(set2)
    print(f'r2 = {r2}')

    # 差集 difference -> - (减)
    r3 = set1.difference(set2)
    print(f'r3 = {r3}')

    # 对称差集 symmetric_difference -> ^ (异或)
    r4 = set1.symmetric_difference(set2)
    print(f'r4 = {r4}')