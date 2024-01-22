# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 19:41
@Auth ： 异世の阿银
@File ：test14.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
自定义异常类
'''
# 自定义异常类
class AgeException(Exception):
    # 初始化方法
    def __init__(self, message):
        # 调用父类初始化方法
        super().__init__(message)

class GenderException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Student:  # 默认继承自object
    # 数据
    def __init__(self, name=None, age=None, gender=None):
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
            # self.__age = 18
            # 抛出异常, raise AgeException 进行异常处理

            raise AgeException('年龄必须在 1 到 120 岁之间!')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        # gender: 只能为男或女, 默认为'保密'
        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            # self.__gender = '保密'
            raise GenderException('性别必须为男或者女.')





    # 行为(方法)
    def introduce(self):
        print(f'大家好, 我叫{self.name}, 我今年{self.age}岁了, {self.gender}')


if __name__ == '__main__':
    try:
        stu1 = Student('张三', 18, '妖')
    except AgeException as e:
        print(e)
    except GenderException as e:
        print(e)
    else:
        stu1.introduce()
    finally:
        print('finally ... ')

    print('程序执行后续代码...')