# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 21:01
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 分支结构的嵌套

# 1.定义两个变量
member = input('亲，您是否为会员？（y是 / n不是）：')
money = int(input('亲，您一共消费了多少钱？:'))

# 2.判断是否为会员
if member == 'y' or member == 'Y':
    # 会员
    if money >= 200:
        # 打8折
        print(f'打8折，需要支付的金额为{money * 0.8}')
    elif money >= 100:
        # 打9折
        print(f'打9折，需要支付的金额为{money * 0.9}')
else:
    # 非会员
    if money >= 200:
        # 打8折
        print(f'打9.5折，需要支付的金额为{money * 0.95}')
    else:
        # 打9折
        print(f'不打折，需要支付的金额为{money}')

print('程序继续向后执行...')