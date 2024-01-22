# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 20:28
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 模拟取钱的执行流程

# 1.定义一个变量代表银行账户存款余额
account = 198

# 2.提示语句
choice = input('欢迎您，ATM机为您服务，需要取现吗？（y取现/n退卡）：')

# 3.判断用户的输入
if choice == 'y' or choice == 'Y':
    # 取现
    print('取现操作中...')
    money = int(input('亲，请输入您的取现金额：'))

    # 判断用户取现的金额是否大于存款的余额
    if money <= account:
        # 余额充足，可以取现
        # 4.1 让余额减少
        account -= money
        print(f'请收好您的取现金额：{money}')
        print(f'您的账户余额为：{account}')
    else:
        # 余额不足，不能取现
        print('余额不足，取现失败！ 还不赶快好好学习，努力赚钱。')

    choice2 = input('亲，您需要执行其他操作还是退卡？Y（退卡）/N(其他操作):')
    # if choice2 != 'y' or choice2 != 'Y':
    if choice2 == 'y' or choice2 == 'Y':
        # 字符串的大小写判断来实现
        # if choice2.lower() != 'y': 超前知识点
        print('退卡中, 请收好您的卡')
    else:
        print('执行其他操作...')
else:
    # 退卡
    print('退卡中，请收好您的卡，下次再会！')