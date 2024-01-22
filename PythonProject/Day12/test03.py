# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/30 21:52
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
学生类

函数 / 方法 有什么区别?
函数: 直接调用传参即可    study(book)
方法: 必须使用具体的对象才可以调用  stu1.study(book)

需求:
# name: 必须两个字符以上, 包含两个字符, 名称不能为习大大, 彭麻麻
# age: 范围[3 ~ 60] 默认为18
# gender: 只能为男或女, 默认为'保密'
'''


class Student:  # 默认继承自object
    # 数据
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 数据的封装 1. property(getter) 2. 属性.setter(setter)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # name: 必须两个字符以上, 包含两个字符, 名称不能为习大大, 彭麻麻
        if isinstance(name, str) and len(name) >= 2 and name not in ['习大大', '彭麻麻']:
            # 数据合法
            self.__name = name
        else:
            self.__name = '无名'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 3 <= age <= 60:
            self.__age = age
        else:
            self.__age = 18

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        # gender: 只能为男或女, 默认为'保密'
        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            self.__gender = '保密'





    # 行为(方法)
    def introduce(self):
        print(f'大家好, 我叫{self.name}, 我今年{self.age}岁了, {self.gender}')


if __name__ == '__main__':
    # 创建一个学生对象
    # 在编程中, 规范大于语法
    stu1 = Student('张三', 18, '男')
    # 调用学生对象的行为
    stu1.introduce()

    # 在创建一个对象
    stu2 = Student('小芳', 16, '女')
    # 调用学生对象的行为
    stu2.introduce()

    # 在创建一个对象
    stu3 = Student('小', 78, '妖')
    # 调用学生对象的行为
    stu3.introduce()




