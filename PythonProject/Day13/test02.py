# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/10 6:52
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
继承: 子类无条件拥有父类中定义的
super 关键字 一般出现在重写方法中

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


class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
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

    def __str__(self):
        return f'Person[name={self.name}, age={self.age}, gender={self.gender}]'


class Student(Person):
    def __init__(self, name, age, gender, stu_id):
        # 此处赋值语言,底层调用对应属性的setter方法   Ctrl+属性名
        # name, age, gender 数据应该从Person类中获取
        # super(Student, self).__init__(name, age, gender)
        # 说明: 从父类中继承来的数据,应传递给父类进行数据的初始化
        super().__init__(name, age, gender)
        # 子类自己的数据,应该子类自己进行数据的初始化
        self.stu_id = stu_id

    @property
    def stu_id(self):
        return self.__stu_id

    @stu_id.setter
    def stu_id(self, stu_id):
        self.__stu_id = stu_id

    def __str__(self):
        # name, age, gender 数据应该从Person类中获取
        info = super().__str__()
        return f'Student[{info}, stu_id={self.stu_id}]'
        # return f'Student[stu_id={self.stu_id}]'


class Teacher(Person):
    def __init__(self, name, age, gender, teaching_field):
        # 此处赋值语言,底层调用对应属性的setter方法   Ctrl+属性名
        # name, age, gender 数据应该从Person类中获取
        super().__init__(name, age, gender)     # 小括号不能省略
        self.teaching_field = teaching_field

    @property
    def teaching_field(self):
        return self.__teaching_field

    @teaching_field.setter
    def teaching_field(self, teaching_field):
        self.__teaching_field = teaching_field

    def __str__(self):
        info = super().__str__()
        return f'Teacher[{info}, teaching_field={self.teaching_field}]'


class SchoolMaster(Person):
    def __init__(self, name, age, gender, working_years):
        # 此处赋值语言,底层调用对应属性的setter方法   Ctrl+属性名
        # name, age, gender 数据应该从Person类中获取
        super().__init__(name, age, gender)
        self.working_years = working_years

    @property
    def working_years(self):
        return self.__working_years

    @working_years.setter
    def working_years(self, working_years):
        self.__working_years = working_years

    def __str__(self):
        info = super().__str__()
        return f'SchoolMaster[{info}, working_years={self.working_years}]'

if __name__ == '__main__':
    stu = Student('张三', 17, '男', '10001')
    print(stu)

    t = Teacher('Jack', 27, '男', 'English and Sport')
    print(t)

    s = SchoolMaster('女校长', 57, '女', '35')
    print(s)

    # 私有化数据, 不能使用stu.name访问, 底层应该是通过对应属性的 @property 方法调用的.
    # Student类中没有该方法, 在调用父类中的init方法后, 才能访问
    print(stu.name, stu.age, stu.gender)