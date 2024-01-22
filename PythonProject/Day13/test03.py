# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/11 6:00
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
Animal类
# 属性
1.name
2.age
# 方法
1.eat
2.run

Dog类继承Animal类
# 特有方法
1.protectedHome
Cat类继承Animal类
# 特有方法
1.catchMouse

ArmyDog类继承Dog类
# 特有方法
1.bombBlockhouse
'''
# 设置按钮->show members 类属性的展示

# 自定义一个'Animal'类
class Animal(object):
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 行为
    def eat(self):
        print(f'{self.age}岁的{self.name}正在疯狂吃东西...')

    def run(self):
        print(f'{self.age}岁的{self.name}正在疯狂裸奔...')

# 自定义一个'Dog'类, 继承自Animal类
class Dog(Animal):
    # 特有方法
    def protectedHome(self):
        print(f'{self.age}岁的{self.name}正在疯狂保护家...')

# 自定义一个'Cat'类, 继承自Animal类
class Cat(Animal):
    # 特有方法
    def catchMouse(self):
        print(f'{self.age}岁的{self.name}正在疯狂抓老鼠...')

# 自定义一个'ArmyDog'类, 继承自Dog类
class ArmyDog(Dog):
    # 特有方法
    def bombBolckhouse(self):
        print(f'{self.age}岁的{self.name}正在疯狂炸碉堡,屌爆了...')


if __name__ == '__main__':
    # Dog类
    dog = Dog('旺财', 2)
    dog.eat()
    dog.run()
    dog.protectedHome()

    # ArmyDog类
    armyDog = ArmyDog('哮天犬', 150)
    armyDog.eat()
    armyDog.run()
    armyDog.protectedHome()
    armyDog.bombBolckhouse()

