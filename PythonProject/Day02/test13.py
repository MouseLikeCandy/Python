# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 21:28
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# Python中没有switch case
'''
    单分支结构
    if bool类型的表达式
    （tab水平制表符） 执行代码体1
    （tab水平制表符） 执行代码体2
    （tab水平制表符） 执行代码体3
    如果成立 就
    if 条件：
        执行语句1
        执行语句2
        执行语句3
'''
# 课堂练习 ：定义变量接收出生年份，判断这个哥们是否成年，如果成年就显示一些信息给他看，否则就算了。
birth_year = int(input('亲，请输入您的出生年份：'))

# 判断
if(2022 - birth_year) >= 18:
    # 如果条件成立，说明这个哥们/姐们成年了
    print('恭喜你，成年了，需要负法律责任了。')

    print(f'这里有很多好玩的东西，一起来玩啊！')
    print(f'这里有很多好看的东西，一起来看啊！')

print(f'程序继续向下执行。。。')


# 条件语句的’缩进‘非常重要，决定了整个整体的作用范围。