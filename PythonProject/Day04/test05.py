# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 6:32
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


'''
循环嵌套
'''
# 定义一个计数器变量
count = 0

# 思考：外层循环多少次？ 10次
for i in range(10):
    for j in range(10):
        # 思考：内层循环多少次？10次
        # 让计数器变量‘计数’
        count += 1

# 最后查看count数值
print(f'count = {count}')


# 外层循环每循环一次，内层循环就‘重新’循环所有次

