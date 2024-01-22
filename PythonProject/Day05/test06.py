# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 21:08
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    range(start,stop,step)
    字符串切片
    字符串可以进行截取（切一小段），这个行为也被称为字符串的'切片'
    
    字符串[start : stop : step]
    1. start    开始 从哪个位置开始切？                           默认为0
    2. stop     结束 切到哪结束？                                默认切到最后
    3. step     步长 怎么切？一个一个切？还是隔一个切？还是隔两个切？ 默认是1
    截取时冒号不能省略
    写法：字符串[数值] 如果只写一个数值，不表示start, stop, step, 表示index下标 
'''

# 定义一个字符串
str = 'hello,python'    # 因为字符串是由一个一个的字符组成的，所以字符串其实是一个序列，序列就会有下标。

print(str)

# 字符串特性
# 1. 字符串有驻留机制
# 2. 字符串是一个序列，序列拥有下标的特性

# 下标index ： 正向下标, 从0开始，从左向右数 str[0]   str[5]   负向下标，从-1开始，从右向左数 str[-12] str[-7]
print(f'正向下标：str[0] = {str[0]}')
print(f'负向下标：str[-12] = {str[-12]}')

# 需求1： 切出hello 子字符串（substring）
# str[0:5:1] 不包含尾部
# str[:5]
print(f'str[0:5:1] = {str[0:5:1]}, str[:5] = {str[:5]}')
# 需求2： 切出python
# str[6:12:1]
# str[6:]
print(f'str[6:12:1] = {str[6:12:1]}, str[6:] = {str[6:]}')

# 需求3： 以下切片会得到什么结果？
# str[::2] =>从头切到尾，步长为2
# hlopto
print(f'str[::2] = {str[::2]}')

# 需求4： str[::] 毫无意义，与源字符串一模一样
# 需求5： str[::-1] 将源字符串倒序拼接
print(f'str[::-1] = {str[::-1]}')
