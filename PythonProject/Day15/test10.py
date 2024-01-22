# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 14:40
@Auth ： 异世の阿银
@File ：test10.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
random
'''

import random

print(dir(random))


# randint
num = random.randint(1, 3)
print(num)

# choice 随机选择
colors = ['red', 'blue', 'green', 'white', 'gray', 'yellow', 'gold', 'purple']
color = random.choice(colors)   # RGB(255, 255, 255)黑色        # RGB(0, 0, 0)白色
print(color)

# sample 采样
samples = random.sample(colors, 3)
print(samples)

# shuffle 洗牌, 打乱顺序
random.shuffle(colors)
print(colors)