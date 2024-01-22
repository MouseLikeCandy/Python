# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/10 6:52
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
继承: 子类无条件拥有了父类中数据和行为

1.学生类
    数据: name, age, gender, stu_id
    行为: __str__返回该对象对应的数据
2.教师类
    数据: name, age, gender, teaching_field
    行为: __str__返回该对象对应的数据
3.校长类
    数据: name, age, gender, working_years
    行为: __str__返回该对象对应的数据
'''


class Student:
    def __init__(self, name, age, gender, stu_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.stu_id = stu_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # return self.__name = name
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def stu_id(self):
        return self.__stu_id

    @stu_id.setter
    def stu_id(self, stu_id):
        self.__stu_id = stu_id

    def __str__(self):
        return f'Student[name={self.name}, age={self.age}, gender={self.gender}, stu_id={self.stu_id}]'

class Teacher:
    def __init__(self, name, age, gender, teaching_field):
        self.name = name
        self.age = age
        self.gender = gender
        self.teaching_field = teaching_field

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # return self.__name = name
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def teaching_field(self):
        return self.__teaching_field

    @teaching_field.setter
    def teaching_field(self, teaching_field):
        self.__teaching_field = teaching_field

    def __str__(self):
        return f'Student[name={self.name}, age={self.age}, gender={self.gender}, stu_id={self.teaching_field}]'

class SchoolMaster:
    def __init__(self, name, age, gender, working_years):
        self.name = name
        self.age = age
        self.gender = gender
        self.working_years = working_years

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # return self.__name = name
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def working_years(self):
        return self.__working_years

    @working_years.setter
    def working_years(self, working_years):
        self.__working_years = working_years

    def __str__(self):
        return f'Student[name={self.name}, age={self.age}, gender={self.gender}, stu_id={self.working_years}]'

if __name__ == '__main__':
    stu = Student('张三', 17, '男', '10001')
    print(stu)

    t = Teacher('Jack', 27, '男', 'English and Sport')
    print(t)

    s = SchoolMaster('女校长', 57, '女', '35')
    print(s)
