# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 21:08
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
定义一个Calculator 计算器类

# 如何判断一个行为应该是对象行为还是类行为?
# 在这个行为当中,有没有用到堆区中的对象
'''

class Calculator:
    # 初始化方法
    def __init__(self, price, color):
        self.price = price
        self.color = color

    # 求和的行为
    # 类方法的调用: 类名.方法名
    @classmethod    # 修饰符: 修改该行为属于 '类行为 / 类方法' , cls -> class 就是当前类, 等同于Calculator这个类
    def get_sum(cls, *args):
        sum = 0
        for num in args:
            sum += num
        return sum


if __name__ == '__main__':
    calc = Calculator.get_sum(10, 20, 30, 40, 50)
    print(f'calc = {calc}')

