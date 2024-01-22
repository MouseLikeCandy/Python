# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/23 20:16
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 扑克牌斗地主

# 导入import random 随机模块
import random
# 创建一幅扑克牌
pokers = []
# 1.1 准备数字
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, k, A]
# 1.2 准备花色

# 1.3 生成对应的扑克牌

# 1.4 添加大小王

# 2. 实现列表元素的 随机洗牌
random.shuffle(pokers)

# 3. 准备三个玩家和底牌
player1 = []
player2 = []
player3 = []
base = []   #底牌

# 4.发牌
for index, poker in poksers:   # enumerate(列表) => (下标,元素)
    # 4.1最后三张属于底牌
    if index >= 51:
        # 底牌
        base.append(poker)
    else:
        # 玩家牌
        if index % 3 == 0:
            # 玩家一
            player1.append(poker)
        elif index % 3 == 1:
            # 玩家二
            player2.append(poker)
        elif index % 3 == 2:
            # 玩家三
            player3.append(poker)
# 5. 看牌
print(f'player1 = {player1}')
print(f'player1 = {player2}')
print(f'player1 = {player3}')
# 6. 随机生成一个地主
landlord = random(1, 3)
print(f'landlord = {landlord}')

# 7. 排序
# 尝试将列表中的字符串元素实现排序
# 按照字符串的排序规则，元素的排序是正确的。
# 按照斗地主的排序规则，元素的排序是错误的。
player1.sort()
player2.sort()
player3.sort()
base.sort()

# 所有的规则我们都可以通过映射表来实现
# 映射表 => 字典
# 自定义游戏规则。 小元素 => 小值小牌  大元素 => 大值大牌

# 1. 玩家手中的牌 => 直接发放数字牌[0~53], 这里要先准备一幅数字牌
# 2. 将数字牌搭乱 / 洗牌
# 3. 将数字牌发给玩家
# 4. 将玩家手中的牌实现排序
# 5. 玩家手中的牌已经有序后，可以从'映射表'中通过key来获取相应的value


