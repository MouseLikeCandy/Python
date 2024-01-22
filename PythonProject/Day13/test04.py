# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/11 7:01
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
多继承:一个子类可以同时拥有多个父类
注意:
慎用多继承: C(A, B)
继承关系最好多重继承: ArmyDog(Dog)  Dog(Animal)  Animal(object) 
'''
class A:
    def method_A(self):
        print('A ...')
    def method_X(self):
        print('A->X ...')
class B:
    def method_B(self):
        print('B ...')
    def method_X(self):
        print('B->X ...')

class C(A, B):
    pass


if __name__ == '__main__':
    c = C()
    c.method_A()
    c.method_B()
    c.method_X()    # 混乱

