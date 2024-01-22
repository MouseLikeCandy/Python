class People(object):
    """
    # 类变量
    name = '二两'

    # 类方法
    def talk(self):
        print('hello')


# 实例化
p1 = People()
p2 = People()
print(p1.name)
print(p2.name)
p1.talk()
p2.talk()
    """

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类中的方法
    def talk(self):
        print(f'你好! 我叫{self.name}, 今年{self.age}岁')


# 实例化
p1 = People('二两', '30')
p2 = People('张三', '25')
print(p1.name)
print(p2.name)
p1.talk()
p2.talk()


# Student类继承People 重写里面的方法
class Student(People):
    #    pass  # 没有编写任何代码, pass表示没有任何逻辑
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def talk(self):
        print(f'你好!我叫{self.name}, 今年{self.age}岁, 就读于{self.school}')


# s1 = Student('学生二两', 23)
# s1.talk()
s2 = Student('张三', 22, '社会大学')
s2.talk()


# Student 对父类People中的方法并不是全部修改
# 可以用到其中的内容

class Student(People):
    def __init__(self, name, age, school):
        # 不需要修改的部分直接继承下来
        super().__init__(name, age)
        # 改动部分
        self.school = school

    def talk(self):
        super().talk()
        print(f'就读于{self.school}')


s3 = Student('老六', 25, '哈佛')
s3.talk()


# 多态
class Teacher(People):
    def __init__(self, name, age, school):
        # super().__init__(self, name, age)
        super().__init__(name, age)
        self.school = school

    def talk(self):
        super().talk()
        print(f'就职于{self.school}')


t1 = Teacher('康师傅', 44, '二高中')
t1.talk()

# isinstance方法可以判断变量是否属于某种类型
print(isinstance(s3, People))
print(isinstance(t1, People))


def talk_something(people):
    if isinstance(people, People):
        people.talk()


s = Student('李斌', 23, '辽宁工程技术大学')
t = Teacher('李铁', 44, '辽宁工程技术大学')
talk_something(s)
talk_something(t)


class Programmer(People):
    # 使用父类的方法

    def talk(self):
        super().talk()
        print('我爱编程')


p = Programmer('林一', 24)
talk_something(p)
