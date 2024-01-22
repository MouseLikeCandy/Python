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

__str()__: 查看对象数据
重写__str()__
# 程序中如果直接输出对象名称, 其实应该显示该对象的数据.
print(stu1) 打印对象名这条语句在系统底层会自动调用 __str__

'''


class Student:  # 默认继承自object
    # 数据
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 重写实现__str()__方法   # 打印,查看对象,底层会自动调用该类的__str()__方法
    def __str__(self):
        return f'Student[name = {self.name}, age = {self.age}, gender = {self.gender}]'
        # 默认调用方式
        # return super.__str__()

    # 行为(方法)
    def introduce(self):
        print(f'大家好, 我叫{self.name}, 我今年{self.age}岁了, {self.gender}')


if __name__ == '__main__':
    # 1. 创建两个学生对象
    stu1 = Student('张三', 18, '男')
    stu2 = Student('戴三', 108, '男')
    print(f'stu1 = {stu1}')
    print(f'stu2 = {stu2}')
    # 调用学生对象的行为

    # 2. 需求: 查看对象的数据
    # introduce() 介绍自己: 主要用来查看对象的数据
    stu1.introduce()









