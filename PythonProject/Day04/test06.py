# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 6:40
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 模拟地球公转、自传
# 循环嵌套的描述：外层每循环一次，内层就会循环所有次

# 1.外层循环（公转）
for i in range(1, 4, 1):
    # 2. 内层循环（自转）
    for j in range(1, 366, 1):
        print(f'地球完成了第{j}次自转')

    print(f'地球完成了第{i}次公转')
