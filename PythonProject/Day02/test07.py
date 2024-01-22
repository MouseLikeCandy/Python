# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:40
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 课堂练习：某超市TShirt的单价是56.5，裤子的单价是89.8，
# 凤姐卖了3件TShirt,5条裤子， 请写程序计算凤姐一共该给多少钱？
# 如果是老板生日，全场88折，凤姐又需要付多少钱呢？

# 1.定义变量,存储数据
t_shirt = float(input('亲，请输入t_shirt的价格：'))
pants = float(input('亲，请输入裤子的单价：'))
t_shirt_count = int(input('亲，您买了几件t_shirt:'))
pants_count = int(input('亲，您买了几条裤子:'))

# 2.数值运算
money = t_shirt * t_shirt_count + pants * pants_count
print(f'money = {money}')

# 3.折扣
discount = 0.88
discount_money = money * discount
print(f'discount_money = {discount_money}')
