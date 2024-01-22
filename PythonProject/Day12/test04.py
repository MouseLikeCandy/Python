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
# 判断两个对象是否相同
== 运算符在底层默认调用__eq__方法   equals
重写__eq()__
eq 与 str
'''


class Student:  # 默认继承自object
    # 数据
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

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

    # 需求: 希望两个对象判断的时候,直接实现数据的判断
    # 实现: 设计该类时, 需要重写object类的__eq__()方法

    # stu1 == stu2
    def __eq__(self, other):
        # self -> 自己, 就是Student类型的对象, 所以self不需要进行类型判断
        # self -> stu1
        # other -> stu2
        if isinstance(other, Student):
            # other 是Student类型对象
            # 接下来判断两个对象的数据是否全部相同
            if self.name == other.name and self.age == other.age and self.gender == other.gender:
                return True
        else:
            # other 不是Student类型对象
            return False

        print(f'-------')
        print(f'self = {self}')
        print(f'other = {other}')
        return True
        # 默认实现
        # return super.__eq__(other)


    # 行为(方法)
    def introduce(self):
        print(f'大家好, 我叫{self.name}, 我今年{self.age}岁了, {self.gender}')


if __name__ == '__main__':
    # 1. 创建两个学生对象
    stu1 = Student('张三', 18, '男')
    stu2 = Student('张三', 18, '男')
    print(f'stu1 = {stu1}')
    print(f'stu2 = {stu2}')
    # 调用学生对象的行为
    stu1.introduce()

    # 2. 判断两个学生是否为同一个人
    # 判断的依据: 如果两个对象的数据完全相同, 那么我们就认为这两个是相同的对象

    result = stu1 == stu2   # 默认判断两个对象在堆中的地址是否相同
    print(f'result = {result}')

    # 对象的本质: 是对象在堆区中存储数据的地址.

'''
如果一个类没有显示继承任何一个类, 那么该类默认继承自object类, 根类
'''

print(dir(Student))





