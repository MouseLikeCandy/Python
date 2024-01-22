# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 21:08
@Auth ： 异世の阿银
@File ：test12.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 逻辑运算符 ： 将多个’布尔类型‘的结果实现组合判断
# 组合有几种类型？ and 并且    or或者   not取反

# 生活： 你找女朋友？你有什么条件？=> 白  并且  富  并且  美  （高富帅）   多个条件同时成立（一假即假）
# 生活： 你找女朋友？你有什么条件？=> 白  或者  富  或者  美             多个条件只要有一个成立就可以（一真即真）
# 生活： 你找女朋友？你有什么条件？=> 是个女的就成立/活的就行

# 需求： 判断一个人是否为男性，并且大于18岁

gender = input('亲，请输入您的性别(F女性/M男性)：')
age = int(input('亲，请输入您的年龄：'))

result = gender == 'M' and age >= 18
result = gender == 'M' or age >= 18
print(f'result = {result}')

r = not True
print(r)

# BUG 漏洞
# DEBUG 计算机排除故障
# 断点 F7

