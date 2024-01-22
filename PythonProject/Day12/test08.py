# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 21:35
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
设计一个Circle类

'''


class Circle:
    # 类数据, 访问时使用类名来访问, 所有对象所共享
    PI = 3.14

    # 初始化数据
    def __init__(self, radius):
        self.radius = radius

    # # 行为: 获取面积
    # def get_area(self):
    #     # 公式: πr²   运算顺序:括号 乘方 乘除 加减
    #     return Circle.PI * self.radius ** 2

    @classmethod
    def get_area(cls, radius):
        return cls.PI * radius ** 2


if __name__ == '__main__':
    # # 创建一个Circle对象
    # c1 = Circle(5)
    # # 获取c1对象的面积
    # area1 = c1.get_area()
    # print(f'area1 = {area1}')
    #
    # # 创建一个Circle对象
    # c2 = Circle(8)
    # # 获取c2对象的面积
    # area2 = c2.get_area()
    # print(f'area2 = {area2}')

    print('-' * 100)
    # 修改类数据
    Circle.PI = 2.14

    # 获取c1对象的面积
    area1 = Circle.get_area(5)
    print(f'area1 = {area1}')
    # 获取c2对象的面积
    area2 = Circle.get_area(8)
    print(f'area2 = {area2}')

'''
类数据: PI = 3.14   在内存中仅有一份, 直接存储在该类的模板中.类数据可以被该类的所有对象共享.
类数据一旦被修改,那么之后的对象再访问该数据, 就是修改之后的数据了.
类行为: @classmethod + cls

对象数据: radius 
对象行为: get_area(self)
'''