# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 8:14
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
多态案例
'''

# 定义一个Animal类
class Animal(object):
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 行为
    def run(self):
        print(f'{self.age}岁的{self.name}正在奔跑.')

    def eat(self):
        print(f'{self.age}岁的{self.name}正在吃饭.')

# Dog
class Dog(Animal):
    # 特有行为
    def bomb_blockhouse(self):
        print(f'{self.age}岁的{self.name}正在炸天宫.')

# Cat
class Cat(Animal):
    # 特有行为
    def mymoe(self):
        print(f'{self.age}岁的{self.name}正在卖萌.')

# Bird
class Bird(Animal):
    # 特有行为
    def pole_dance(self):
        print(f'{self.age}岁的{self.name}正在跳钢管舞.')

# Person
class Person(object):
    # 数据
    def __init__(self, name):
        self.name = name

    # 行为
    def feed_animal(self, animal):
        # 公有行为, 不需要类型判断, 可以直接使用
        animal.run()
        animal.eat()
        # 私有行为, 调用前必须要判断类型
        if isinstance(animal, Cat):
            animal.mymoe()
        if isinstance(animal, Dog):
                animal.bomb_blockhouse()
        if isinstance(animal, Bird):
            animal.pole_dance()

        # 该方法内需要执行的其他行为
        print(f'{animal.name}吃饱后对{self.name}疯狂摇尾巴...')

if __name__ == '__main__':
    # 创建一个Person类型的对象
    monkey_king = Person('孙悟空')

    # 创建一些Animal类型的子类对象
    dog = Dog('哮天犬', 120)
    cat = Cat('波斯猫', 3)
    bird = Bird('鹦鹉', 5)

    monkey_king.feed_animal(dog)