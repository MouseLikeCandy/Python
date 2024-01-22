# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 20:13
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 循环流程控制关键字 continue 结束本次循环继续下次循环
# continue之后的循环体代码就不会被执行了。

for i in range(10):
    # 判断
    if i == 5:
        break
    print(i, end='\t')

print()

for i in range(10):
    # 判断
    if i == 5:
        continue
    print(i, end='\t')

