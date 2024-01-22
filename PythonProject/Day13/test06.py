# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 6:12
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
多态: 多种状态/形态
同一个行为,对于不同的对象,会出现截然不同的执行状态
同一个行为,对于传入不同的对象,具有完全不同的表现形式
多态的基础是继承

思考: 听到cut单词的时候, 脑海中会有什么行为?

1.理发师 -> 剪发
2.演员   -> 停止表演
3.医生   -> 开刀

Person类
子类: Barber理发师 Actress女演员 Doctor医生

继承一般要满足 is a 的语法.
1. Barber is a Person.
2. Actress is a Person.
3. Doctor is a Person.
多态一般在程序中体现在方法的参数上, 在定义一个方法的时候,一般会将参数定义为父类类型.
在使用时,调用者应该传递该父类具体的子类对象.
程序执行时:
1.可以直接执行父类中定义的行为.如果子类没有重写,直接调用父类该行为.
    如果子类重写了,程序就会调用子类重写的该行为.
    如果子类重写中需要使用父类该行为,语法super().方法名().[可选]
2.多态的代码体现: 父类类型传递子类对象,执行子类不同的行为.

Python预言是攻台语言.
虽然cut行为定义了Person类型的对象, 但是调用者可以传入任何类型的对象.
其他语言: 多态语法必须这样写cut(Person person) 参数名之前必须指定参数类型.其他语言的变量是有类型的.
    如果传递的不是Person类型的对象, 程序不用运行, 编译器就会报错.

Python语言是解释型语言,没有编译过程.程序是一句句代码直接执行的.
编译: 将源代码翻译成0,1.让所有的源代码翻译完成后执行.
'''


# 定义一个Person类
class Person(object):
    # 属性
    # 行为
    def do_something(self):
        print('Person类正在做XXOO...')


class Barber(Person):
    # 子类重写父类行为
    def do_something(self):
        print('理发师正在认真细致的剪头发.')

    # 特有行为
    def chasing_girls(self):
        print('理发师正在追女孩...')


class Actress(Person):
    # 子类重写父类行为
    def do_something(self):
        print('女演员停止了表演.')

    # 特有行为
    def be_famous(self):
        print('女演员正走在成名的潜规则道路上.')


class Doctor(Person):
    # 子类重写父类行为
    def do_something(self):
        print('女医生正在为你准备开膛破肚...')

    # 特有行为
    def uniform_temptation(self):
        print('女医生正在手术台上对你进行制服诱惑.')


# 设计一个函数'cut'行为  Person类的所有子类都可以传入
# cut(传入的Person对象) 定义时参数使用父类类型的对象, 真正传递的时候, 传递的是具体的子类类型对象.
#   执行行为...
# 思考: 如果子类中有子类特有的行为,那么在cut方法中如何执行子类特有的行为呢?
# 公有行为 + 私有行为 = 对象的所有行为
def cut(person):
    # 执行人类对象的共有行为
    person.do_something()
    # 哪个方法可以判断对象的具体类型? isinstance(对象, 类型) -> bool类型的结果
    if isinstance(person, Barber):
        person.chasing_girls()  # 该代码仅对Barber对象能正常执行, 其他Person类就会报错.
    if isinstance(person, Actress):
        person.be_famous()
    if isinstance(person, Doctor):
        person.uniform_temptation()

if __name__ == '__main__':
    barber = Barber()
    actress = Actress()
    doctor = Doctor()
    # 调用cut行为, 将理发师对象传入
    # 思考: 理发师听到cut, 应该做什么?
    # 思考: 女演员听到cut, 应该做什么?
    # 思考: 女医生听到cut, 应该做什么?

    # 多态: 对于一个行为而言, 传入不同的对象, 就会产生不同的行为状态
    cut(barber)
    cut(actress)
    cut(doctor)
