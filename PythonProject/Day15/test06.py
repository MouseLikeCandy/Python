# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 14:16
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time

'''
time

# 时间戳 timestamp
可以用来测试程序运行的时间

# 程序中到底是什么代码最消耗性能呢?   运算 + 赋值
'''
import time
start = time.time()

# 执行一段程序
sum = 0
for i in range(100000000):
    sum += i

end = time.time()

print(end - start)

