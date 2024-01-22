# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/11 7:08
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
重写
1. 子类没有重写父类的行为
程序执行时,直接执行父类中继承的该行为.
2. 子类重写了父类的行为
程序执行时,仅执行子类中重写的该行为.
3. 子类重写了父类的行为
在子类重写行为中,如果子类希望执行父类中原先的行为,需要通过super().方法名()执行父类行为.

继承体系中方法调用的顺序:
在子类中,调用一个对象方法
1.首先会在子类中查找该方法.
2.如果子类中没有,那么向上一层父类中查找.
3.如果上一层父类中也没有,再向上一层爷爷中查找.
4.直到object类,如果还是没有,直接报错.
注意: 如果上面某一层中找到了该方法,那么直接调用不会再向上查找了.

Python 方法命名规则: 全小写/下划线分隔

# 思考: 子类继承父类, 子类就会无条件拥有父类中的所有行为和数据.
# 如果子类的行为与父类的行为不一致时,子类如何做呢?

# 子类可以重写父类中该行为.
# 子类一旦重写父类的行为, 程序执行时, 执行子类重写的行为, 父类中原先的行为就不会执行了.

# 如果子类重写了父类行为, 但是在子类实现中, 子类需要执行父类中原来行为,该怎么办?
# self  自己
# super 父类

'''
# 自定义一个Person类
class Person(object):
    def sayhi(self):
        print('Person: 大家好!我是人类!')

class Chinese(Person):
    # 如果子类的行为与父类不一致, 此时,子类就可以重写父类的该行为. override
    def sayhi(self):
        print('中国人打招呼: 嘿, 你吃饭了吗?')

class Japanese(Person):
    def sayhi(self):
        # super(对象类型, 对象) 参数默认是不需要传递的
        # super(Japanese, self).sayhi()
        super().sayhi()
        print('日本人打招呼: 亚麻得, 八嘎?')

class Korean(Person):
    def sayhi(self):
        print('韩国人打招呼: 阿尼哈斯有, 泡菜思密达?')


if __name__ == '__main__':
    c = Chinese()
    c.sayhi()

    j = Japanese()
    j.sayhi()

    k = Korean()
    k.sayhi()