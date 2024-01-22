# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/23 20:50
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 生成映射表
'''
# 1. 玩家手中的牌 => 直接发放数字牌[0~53], 这里要先准备一幅数字牌
# 2. 将数字牌搭乱 / 洗牌
# 3. 将数字牌发给玩家
# 4. 将玩家手中的牌实现排序
# 5. 玩家手中的牌已经有序后，可以从'映射表'中通过key来获取相应的value
'''
import random

# 1. 准备一个映射表
# 1.1 准备对应的值
numbers = [str(i) for i in range(3, 11, 1)]
numbers.extend(['J', 'Q', 'K', 'A', '2'])
# 1.2 准备花色
colors = []
# 1.3 遍历
poker_dict = []
poker_key = 0   # 注意：一般从零开始比较好
for number in numbers:
    for color in colors:
        poker = number + color
        poker[poker_key] = poker
        poker_key += 1

# 1.4 添加大小王
poker.append()
# 2. 定义一幅数字牌
number_pokers = [i for i in range(54)]
print(number_pokers)

# 3. 打乱数字牌
random.shuffle(number_pokers)
print(number_pokers)

# 4. 准备三个玩家和底牌
player1 = []
player2 = []
player3 = []
base = []   #底牌

# 5. 发牌
for index, number_poker in enumerate(number_pokers):  # 发给玩家的数字
    print(number_poker)     # (下标, 元素)
    # 4.1最后三张属于底牌
    if index >= 51:
        # 底牌
        base.append(number_poker)
    else:
        # 玩家牌
        if index % 3 == 0:
            # 玩家一
            player1.append(number_poker)
        elif index % 3 == 1:
            # 玩家二
            player2.append(number_poker)
        else:
            # 玩家三
            player3.append(number_poker)

# 6. 先给玩家手中的牌排序
player1.sort()
player2.sort()
player3.sort()
base.sort()
# 看牌
print(f'player1 = {player1}')
print(f'player2 = {player2}')
print(f'player3 = {player3}')
print(f'base = {base}')

# 7. 玩家根据自己手中的牌从映射表中取出对应的值
# 思考：学习完函数之后，如何改进这段代码
player1_poker = []
player2_poker = []
player3_poker = []
base_poker = []
for poker_key in player1:
    poker = poker_dict[poker_key]
    player1_poker.append(poker)

# 8. 查看扑克牌
print(f'player1_poker = {player1_poker}')
print(f'player1_poker = {player1_poker}')
print(f'player1_poker = {player1_poker}')
print(f'base_poker = {base_poker}')

# 9. 随机生成一个地主
landlord = random(1, 3)
print(f'landlord = {landlord}')

