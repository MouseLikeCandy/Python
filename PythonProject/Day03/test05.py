# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 20:12
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 需求：根据数值判断月份

# 1.让用户输入对应的月份数值
month = int(input('亲，请输入月份：'))
# 2.根据数值判断月份
if month == 3 or month == 4 or month == 5:
    print(f'{month}对应的季节为：春季')
elif month == 6 or month == 7 or month == 8:
    print(f'{month}对应的季节为：夏季')
elif month == 9 or month == 10 or month == 11:
    print(f'{month}对应的季节为：秋季')
elif month == 12 or month == 1 or month == 2:
    print(f'{month}对应的季节为：冬季')
else: # 兜底方案，简化分支结构的嵌套
    # 以上所有条件都不满足，最后执行else语句
    print('恭喜你，在一个特别的星球上...')


print('程序继续向下执行...')