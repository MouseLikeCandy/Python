# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 18:15
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 1~100之间3的倍数的个数

# 1.定义一个循环变量
i = 1
# 定义一个‘框’变量
count = 0


# 2. 循环条件
while i < 100:

    # 条件
    if i % 3 == 0:
        print(i, end='\t')
        # 计数
        count += 1
    # 循环增量
    i += 1

print(i)
