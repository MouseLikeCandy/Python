# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 21:19
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 列表的特点
# 元素有序（放入顺序）存取有序
'''
    列表的特点
    1.元素存取有序
    2.元素有索引
    3.元素可重复
    4.列表的长度是动态可扩展的
'''
# 字符串排序
# 定义一个国家名称的列表数据
country_list = ['China', 'America', 'Russia', 'India', 'Canada', 'Japan', 'South Korea', 'North Korea', 'France', 'German']
country_list.sort()
print(country_list)

# 字符串排序规则
# 先比较首字母，如果首字母直接有结果了，后续字母就不会再比较了
# 一个一个字符，底层一个一个数字比，如果第一个数字一样，那就再比第二个数字，往后全部以此类推

# 字符 -> 数值    （ASCII 字符编码表）
# ASCII (American Standard Code for Information Interchange)：美国信息交换标准代码
