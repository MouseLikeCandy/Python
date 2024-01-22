# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 21:51
@Auth ： 异世の阿银
@File ：str_split.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import random

'''
# ♣♦♠♥    大王 ♚    小王 ♛
# 需求: 使用斗地主的规则实现发牌和洗牌
# 1. 54张牌
# 2. 3个人玩
# 3. 每个人17张牌,余3张牌. 54/3=17...3
# 4. 地主拥有最后3张牌
# 5. 谁是地主? 随机
'''

# 1. 购买一幅扑克牌 / 创建一幅扑克牌
# 2♣ 2♦ 2♠ 2♥ 3♣ 3♦ 3♠ 3♥ ....A♣ A♦ A♠ A♥ 大♚ 小♛
pokers = []
# 1.1 准备数字牌
numbers = []
for i in range(2, 11, 1):
    # 将 i 转为字符串
    numbers.append(str(i))
# ['J', 'Q', 'K', 'A']
numbers.extend(['J', 'Q', 'K', 'A'])
print(numbers)

# 1.2 准备花色牌
colors = ['♣', '♦', '♠', '♥']
print(colors)

# 1.3 实现数字与花色的拼接
for number in numbers:
    for color in colors:
        poker = number + color
        # 将拼接完成的每一张扑克牌存储到 pokers 列表中
        pokers.append(poker)
print(pokers)

# 1.4 完成最后大小王的存储
pokers.append('小♛')
pokers.append('大♚')
print(pokers)
print(len(pokers))

# 2.发牌之前要先洗牌(列表中的元素实现乱序)
# random.randint(a, b) 完成a~b之间的随机整数获取
# random.shuffle(列表名) 完成列表的随机洗牌

import random
# Shuffle list x in place, and return None. 对列表中的所有元素实现随机存储(洗牌)
random.shuffle(pokers)
print(pokers)

# 3. 发牌
# 3.1 准备3个玩家和一个底牌
player1 = []
player2 = []
player3 = []
base_pokers = []

# 3.2 遍历 pokers 列表
# for poker in pokers:
    # 3.3 发牌, 玩家还是 底牌(最后三张留给底牌)
    # 请问: 最后三张是哪三张?
    # print(poker)

# enumerate 迭代器, 元组 下标
for index, poker in enumerate(pokers):
    # 3.3 发牌, 玩家还是 底牌(最后三张留给底牌)
    # 请问: 最后三张是哪三张?
    print(index, poker)
    if index >= 51:
        # 底牌
        base_pokers.append(poker)
    else:
        # 玩家, 三个玩家怎么发牌? index % 3 -> 0, 1, 2 有三种可能性
        if index % 3 == 0:
            # 玩家一
            player1.append(poker)
        elif index % 3 == 1:
            # 玩家二
            player2.append(poker)
        elif index % 3 == 2:
            # 玩家三
            player3.append(poker)

# 4. 查看扑克牌
# 回顾字符串的排序规则: 一个一个字符进行比较, 一旦有结果, 立即返回, 后续字符不在比较
player1.sort()  # 是字符串的排序规则
# 思考: 如何实现斗地主的排序规则,自定义的排序规则?
print('浅梦', player1)
# print('浅梦', player1.sort())   sort()没有返回结果, 不能打印
print('天空', player2)
print('银河', player3)
print('底牌', base_pokers)
print('地主', random.randint(1, 3))

'''
# ♣♦♠♥    大王 ♚    小王 ♛
# 能不能将自定义的规则形成一种排序的关系? '映射表' / key -> value   字典
# 3♣ 3♦ 3♠ 3♥ 4♣ 4♦ 4♠ 4♥....A♣ A♦ A♠ A♥ 2♣ 2♦ 2♠ 2♥
# {0:3♣, 1:3♦, 3♠ 3♥ 4♣ 4♦ 4♠ 4♥....A♣ A♦ A♠ A♥ 2♣ 2♦ 2♠ 2♥ 52:小♛, 53:大♚}
'''

# 1. 自定义一张'映射表', 反映的就是斗地主的自定义规则
pokers_dick = {}
numbers = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
colors = ['♣', '♦', '♠', '♥']

# 定义一个映射表的key
index_key = 0
for number in numbers:
    for color in colors:
        poker = number + color
        print(poker)
        # 将每一张扑克牌存储到'扑克牌映射表'字典中
        pokers_dick[index_key] = poker
        # index_key 需要自增
        index_key += 1
# 最后拼接'大小王'
pokers_dick[index_key] = '小♛'
index_key += 1
pokers_dick[index_key] = '大♚'
print(pokers_dick)

# 2. 准备一副发给玩家的'数字'扑克牌, 最后玩家根据手中的数字牌(key), 从映射表中获取对应的'扑克牌' value.
poker_numbers = [i for i in range(54)]
print(poker_numbers)

# 3. 洗牌
import random
random.shuffle(poker_numbers)
print(poker_numbers)

# 4. 发牌
player1 = []
player2 = []
player3 = []
base_pokers = []
for index, number in enumerate(poker_numbers):
    # 底牌
    if index >= 51:
        base_pokers.append(number)
    else:
        # 玩家
        # 下标 % 3 -> 确定发牌的顺序
        if index % 3 == 0:
            player1.append(number)
        elif index % 3 == 1:
            player2.append(number)
        elif index % 3 == 2:
            player3.append(number)
print(f'player1 = {player1}')
print(f'player2 = {player2}')
print(f'player3 = {player3}')
print(f'base_pokers = {base_pokers}')

# 5. 将玩家和底牌中的所有数值实现排序
player1.sort()
player2.sort()
player3.sort()
base_pokers.sort()

print(f'player1 = {player1}')
print(f'player2 = {player2}')
print(f'player3 = {player3}')
print(f'base_pokers = {base_pokers}')

# 6. 根据玩家手中的有序的数字牌, 从'斗地主的映射表'中取出对应的扑克牌
poker1_list = []
for poker_key in player1:
    poker = pokers_dick[poker_key]
    poker1_list.append(poker)
print(f'poker1_list = {poker1_list}')

poker2_list = []
for poker_key in player2:
    poker = pokers_dick[poker_key]
    poker2_list.append(poker)
print(f'poker2_list = {poker2_list}')

poker3_list = []
for poker_key in player3:
    poker = pokers_dick[poker_key]
    poker3_list.append(poker)
print(f'poker3_list = {poker3_list}')

base_list = []
for poker_key in base_pokers:
    poker = pokers_dick[poker_key]
    base_list.append(poker)
print(f'底牌 = {base_list}')

print('地主 = {random.randint(1, 3)}')


