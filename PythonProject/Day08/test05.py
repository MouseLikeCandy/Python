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
colors = ['♥', '♦', '♠', '♣']
# 1.3 遍历
poker_dict = {}
poker_key = 0  # 注意：一般从零开始比较好
for number in numbers:
    for color in colors:
        poker = number + color
        poker_dict[poker_key] = poker
        poker_key += 1

# 1.4 添加大小王
poker_dict[poker_key] = '♔'
poker_key += 1
poker_dict[poker_key] = '♕'

print(f'生成映射关系表:\n{poker_dict}')
# 2. 定义一幅数字牌 (与下标一一对应)
number_pokers = [i for i in range(54)]
print(number_pokers)

# 3. 打乱数字牌
random.shuffle(number_pokers)
print(number_pokers)

# 4. 准备三个玩家和底牌
player1 = []
player2 = []
player3 = []
base = []  # 底牌

# 5. 发牌
for index, number_poker in enumerate(number_pokers):  # 发给玩家的数字
    print(index, number_poker)  # (下标, 元素)
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
# 定义一个功能 / 函数, 传递给函数一个数字列表, 返回一个扑克牌结果的列表
# 翻译: 通过映射关系, 进行一个转换, 将数字牌转为实际对应的扑克牌
def get_pokers(num_poker):
    real_poker = []
    for poker_key in num_poker:
        poker = poker_dict[poker_key]
        real_poker.append(poker)
    return real_poker


# 调用函数
player1_poker = get_pokers(player1)
player2_poker = get_pokers(player2)
player3_poker = get_pokers(player3)
base_poker = get_pokers(base)

# 8. 查看扑克牌
print(f'player1_poker = {player1_poker}')
print(f'player2_poker = {player2_poker}')
print(f'player3_poker = {player3_poker}')
print(f'base_poker = {base_poker}')

# 9. 随机生成一个地主
landlord = random.randint(1, 3)
print(f'landlord = {landlord}')
