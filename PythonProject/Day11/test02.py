# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/30 20:01
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
面向对象的三大特性: 封装 继承 多态

很多程序设计语言, 实现对象数据封装通过 get/set 方法实现.
Java语言: age  一个数据属性就需要两个不同名称的方法实现数据的封装.(复杂/麻烦)
1.设置数据
setAge(){ if 判断 ... this.age = age }
2.获取数据
getAge(){ return this.age }

Python语言在对象数据的封装上实现了'超越性'的突破.
关键字:@property 实现了整个数据属性的封装. 并且名称都是一样的.
并且数据属性的获取和设置都是Python底层自动实现调用.

age = dog1.age 获取age属性
dog1.age = 10  设置age属性
'''


# 需求: 设计一个Dog类. 数据: name, age, gender 行为跑,吃,叫...
#

# 设计一个Dog类
# 设计者: 希望所有的数据都是合理的. 那么设计者如何控制数据的合理性?
class Dog:
    # 数据
    # 需求: Dog类实现数据控制, 范围[1 ~ 20]
    def __init__(self, name, age, gender='雌性'):
        # 问题: 如何将栈区中的数据存储到堆区中? self.
        self.name = name
        # 此处虽然可以实现数据的过滤,但不规范
        # age数据实现过滤
        # if 1 <= age <= 20:
        #     self.age = age
        # else:
        #     # 数据错误
        #     self.age = 1
        self.age = age              # 赋值: 默认会调用该属性的setter方法
        self.gender = gender

        # 需求: Dog类实现数据控制, 范围[1 ~ 20]
        # print(f'姓名: {dog1.name}, 年龄: {dog1.age}, 性别: {dog1.gender}')  由dog1.age调用age属性的@property方法
    @property  # 属性,就是成员变量, 就是对象数据, @property表示数据的获取, 默认调用该属性的getter方法
    def age(self):
        print('age -> getter ...')
        return self.__age  # 私有数据都是以__双下划线开头的, 外部不允许访问, 只能在该类的内部使用

    # 由self.age = age调用@age.setter方法
    @age.setter  # 设置数据
    def age(self, age):
        print('age -> setter ...')
        if 1 <= age <= 20:
            self.__age = age
        else:
            # 数据错误
            self.__age = 1  # 默认处理


if __name__ == '__main__':
    # 使用者: 使用者传递数据,可以根据使用者自己的想法随便乱传.
    # 创建一个Dog
    dog1 = Dog('旺财', 2, '雄性')
    # 说明: 如果直接输出'对象', 结果为该对象在内存中的地址. 对象<-->地址
    print(dog1)

    # 查看
    print(f'姓名: {dog1.name}, 年龄: {dog1.age}, 性别: {dog1.gender}')
    # 访问dog1中的私有数据, 不可以访问, 因为私有数据外部无权访问.
    # AttributeError: 'Dog' object has no attribute '__name'
    # print(f'姓名: {dog1.__name}, 年龄: {dog1.__age}, 性别: {dog1.__gender}')
    print('-' * 100)

    # 创建一个Dog
    dog2 = Dog('黄花菜', 5, )
    # 查看
    print(f'姓名: {dog2.name}, 年龄: {dog2.age}, 性别: {dog2.gender}')

# init()方法中的代码是规范性代码, 不要做任何数据的逻辑判断
