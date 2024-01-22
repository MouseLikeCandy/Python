# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 15:14
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
文件写入: 写入数据到硬盘文件中
CPU -> 内存 -> 硬盘
'''

# 相对路径: 相对于当前工作目录
# wt  write text 写入文本文件, 需要指定编码. 如果不指定, 默认为utf-8, t可以省略
# wb  write b
# 打开文件
# 如果文件已经存在, 会覆盖掉原来文件中的数据.
file = open('file.txt', 'wt', encoding='utf-8')
# 执行写入, write写入方法, 并不执行换行.
file.write('你好!\n')
file.write('我好!\n')
file.write('大家好!\n')

# 关闭文件
file.close()

