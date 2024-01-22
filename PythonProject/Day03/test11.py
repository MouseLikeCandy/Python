# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 21:14
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 游戏： 石头剪刀布

# 1.让计算机生成一个随机数
import random
computer = random.randint(1, 3,)
# 作弊
print(f'computer = {computer}')
# 2.让用户输入一个数值
jack = int(input('亲，请输入您的招数（1-石头，2-剪刀，3布）：'))

# 3.判断  and执行优先级高于or
if (jack == 1 and computer == 2) or (jack == 2 and computer == 3) or (jack == 3 and computer == 1):
    print('哈哈哈哈。。。。我Jack天下无敌')
elif jack == 1 and computer == 3 or jack == 2 and computer == 1 or jack == 3 and computer == 2:
    print('jack别吹了，我才是赢家！')
else:
    print('平局，不服，再来一次！')