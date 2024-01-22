# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 21:01
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 字符串   replace替换
'''

str = 'hello, Python, Python'
# replace(old, new, count)
# Return a copy with all occurrences of substring old replaced by new.
# 字符串被修改了，显然产生了一个新的字符串，地址也不相同。
# 说明：count 可以指定替换的次数。(count 是一个位置参数，不是关键字参数)
# 默认可以不传递count，默认替换出现的所有子串
# 将Python替换为China
result = str.replace('Python', 'China')
print(f'result = {result}')

result = str.replace('Python', 'China', 1)  # 替换次数1
print(f'result = {result}')


'''
# 字符串   join拼接
'''
# 定义一个表示国家的列表
country_list = ['China', 'Russia', 'America', 'Canada', 'France']
# 使用->符号连接所有的国家名称
# 遍历国家名称列表
# 获取列表的长度len(country_list)适用于遍历方式：for + range(数字)
# 列表是一个’序列‘，可以直接使用for循环变量
for country in country_list:
    print(country, end='')
    print('->', end='')


# 思考：字符串有没有连接的方法？
# 注意：一定要使用字符串.()查找
result = '->'.join(country_list)
print(result)
