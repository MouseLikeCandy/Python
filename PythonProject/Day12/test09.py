# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 21:56
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
设计类时的'静态方法'
'''

class Game:
    # 初始化数据

    # 静态行为: 展示界面
    # 特点: 不需要访问对象和类的数据

    @staticmethod   # 静态修饰符: 该方法中没有默认参数
    def show_menu(game_name):
        print(f'欢迎来到{game_name}游戏')
        print(f'1. 开始游戏')
        print(f'2. 继续游戏')
        print(f'3. 结束游戏')

if __name__ == '__main__':
    Game.show_menu('坦克大战')

# 静态行为: @staticmethod + 无参
# 特点: 没有默认(self, cls)参数
# 一般情况下, 在静态行为中不会访问数据
# 如果有数据, 这些数据一般是由参数传递进来的
