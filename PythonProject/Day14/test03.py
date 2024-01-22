# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 8:31
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
类方法:    类方法中不能直接访问对象数据, 可以访问类数据. 类数据仅存在一份,被该类的所有对象所共享.(代码区)
对象方法:  对象方法可以直接访问堆区中的对象数据. 方法执行是经过堆区调用的.
静态方法:  不访问类数据和对象数据.

选择最合理的设计
'''
class Game(object):
    # 静态方法, 没有默认参数, 但是可以从调用处直接传递参数
    @staticmethod
    def show_menu(name):
        print(f'欢迎来到 [{name}] 游戏')
        print(f'开始游戏请按[1]')
        print(f'暂停游戏请按[ESC]')
        print(f'结束游戏请按[0]')

    # 类数据

    # 对象数据  def __init()__()

    # 类方法   @classmethod 第一个参数cls

    # 对象方法  第一个参数self


if __name__ == '__main__':
    # 静态方法, 类名调用
    Game.show_menu('贪吃蛇')