# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 20:02
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 练习

# 快捷键：shift + 换行 =》跳到下一行
# 1.定义字符串变量，输出我的名字叫 小明，请多多关照！
name = '小明'
print(f'我的名字叫 {name} ，请多多关照！')
print('我的名字叫 %s ,请多多关照！' % (name,))

# 2.定义整数变量student_no,输出我的学号000001
student_no = 1  # 数值（十进制）
print('我的学号是 %06d' % (student_no,))  # 输出数值6位，不足用零补齐
print('我的学号是 %.6d' % student_no)

# 3.定义小数price、weight、money，输出苹果单价9.05元/斤，购买了5.5斤，需要支付???元
price = 9.05
weight = 5.5
money = price * weight
print(f'苹果单价{price}元/斤，购买了{weight}斤，需要支付{money}元')
print(f'苹果单价%.2f元/斤，购买了%.1f斤，需要支付%.3f元' % (price, weight, money))

# 4.定义一个小数scale，输出数据比例是10.00%
scale = 10.00
print(f'数据比例是{scale}%%')  # f一个%是可以直接使用的
print('数据比例是%.2f%%' % (scale,))  # 如果希望显示一个%，需要书写%%

# 转义字符 ： 特殊含义字符
'''
%   %%
n   \n  换行符
t   \t  水平制表符
\   \\  表示一个\
r   \r  将光标移动到行首 
'''
