# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 9:58
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    综合案例: 学生管理系统V2

    V1 版本关于学生数据的存储不合理.
    v2 版本将所有学生相关的数据, 存储到Student类型对象中
    stu = [stu1, stu2, stu3,...] 好处: 未来可以扩展学生类的数据和行为.
    
    步骤1: 定义一个学生类
    步骤2: 定义一个管理学生的类
'''


# 1. 定义一个学生类
class Student(object):
    # 初始化数据
    def __init__(self, stu_id, name, age, score):
        self.stu_id = stu_id
        self.name = name
        self.age = age
        self.score = score

    # 数据的封装练习 - 私有化
    @property
    def stu_id(self):
        return self.__stu_id

    @stu_id.setter
    def stu_id(self, stu_id):
        if isinstance(stu_id, str):
            pass
        else:
            pass
        self.__stu_id = stu_id

    # 显示数据
    def __str__(self):
        return f'Student[stu_id={self.stu_id}, name={self.name}, age={self.age}, score={self.score}]'


# 2. 定义一个学生管理类
class StudentManager(object):
    # 静态方法, 没有访问类数据
    @staticmethod
    def show_menu():
        while True:
            # 1. 界面展示
            menu = '''
            ----- 欢迎来到学生管理系统 V 2.0-----
                1.查看所有学生
                2.添加学生
                3.修改学生
                4.删除学生
                5.退出程序
            '''
            print(menu)
            # 2. 提示用户输入操作码
            choice = input('亲, 请输入执行的操作码: ')
            # 3. 用户操作码的判断
            if choice == '1':
                # 查看所有学生
                StudentManager.query_students()     # query_students是一个类方法: 类名.类方法
            elif choice == '2':
                # 添加学生
                StudentManager.add_students()
            elif choice == '3':
                # 修改学生
                StudentManager.update_students()
            elif choice == '4':
                # 删除学生
                StudentManager.delete_students()
            elif choice == '5':
                # 退出程序
                print('感谢您的使用,下次再会!')
                break
            else:
                # 操作码不在指定范围内,提示错误
                print('亲, 操作码错误,请重新输入操作码')

    # 定义一个stus列表存储学生数据
    stus = []

    # 使用Student类数据, 定义为类方法
    # 1. 查看所有学生
    @classmethod
    def query_students(cls):
        print(f'查询学生')
        # 1.确保stus中有数据
        if len(cls.stus) == 0:
            # 条件成立,列表为空
            print(f'亲, 目前没有任何学生数据')
            return
        print('-' * 100)
        # 2.遍历stus
        for stu in cls.stus:
            print(stu)

    # 2. 添加学生
    @classmethod
    def add_students(cls):
        print(f'添加学生')
        while True:
            # 1.1 stu_id一定保证不能重复
            stu_id = input('亲, 请输入添加的学生学号, 如(1001):')
            # 1.2 遍历stus列表,取出列表中的所有stu对象, 判断输入的stu_id是否与存在的stu对象的stu_id相同.
            for stu in cls.stus:
                if stu_id == stu.stu_id:
                    # 条件成立, 说明用户输入的stu_id已经被占用
                    print(f'stu_id = {stu_id}已经存在了')  # 一旦学号重复,需要提示用户重新输入学号
                    break  # 跳出for循环
            else:  # 表示for循环正常结束后执行到额代码, 没有遇见break
                print(f'stu_id = {stu_id}可以被使用')
                break  # 跳出while True循环
        # 2. name, age, score
        name = input('亲, 请输入学生的姓名:')
        age = input('亲, 请输入学生的年龄:')
        score = input('亲, 请输入学生的成绩:')

        # 3. 将用户输入的数据包装为学生对象
        # 学生信息对象格式
        stu = Student(stu_id, name, age, score)
        cls.stus.append(stu)
        print(f'添加成功')

    # 3. 修改学生, 学号存在可修改
    @classmethod
    def update_students(cls):
        print(f'修改学生')
        # 根据学生的学号进行学生信息修改
        stu_id = input('亲, 请输入需要修改的学生学号: ')
        # 2. 判断stu_id是否在stu对象中存在
        stu_index = -1
        flag = False  # 表示用户输入的stu_id默认在stus列表中找不到
        for stu in cls.stus:
            stu_index += 1  # 控制并记录当前遍历的学生列表对象的下标位置
            # 3. 判断stu_id是否一致
            if stu_id == stu.stu_id:
                # 学号存在
                flag = True
                print(stu)
                break
            else:
                # 学号不存在
                flag = False
                print(f'没有该学号的学生数据')

        # 4. 提示用户输入该学号对应学生的新的name, age, score
        if flag:
            # 输出已存在的学生信息
            print(cls.stus[stu_index])
            # 提示修改
            name = input('亲, 请输入学生新的姓名:')
            age = input('亲, 请输入学生新的年龄:')
            score = input('亲, 请输入学生新的成绩:')
            # 包装新数据
            new_stu = Student(stu_id, name, age, score)
            # 替代 stus 列表中原来对应的数据
            cls.stus[stu_index] = new_stu
        else:
            print('学号不存在, 无法修改!')

    # 4. 删除学生
    @classmethod
    def delete_students(cls):
        print(f'删除学生')
        # 根据学生stu_id删除学生
        # 1.提示用户输入要删除的学生学号
        stu_id = input('亲, 请输入需要删除的学生学号: ')
        # 2. 判断stu_id是否在stus列表中存在
        # 定义一个学生下标的变量
        flag = False
        stu_index = -1  # 不要写0, -1 是不正常的下标
        for stu in cls.stus:
            stu_index += 1
            if stu_id == stu.stu_id:
                # 条件成立,stu_id存在
                flag = True
                break  # 跳出for循环
        # 3. 判断flag
        if flag:
            # 学生学号找到了
            print(cls.stus[stu_index])
            # 3.2 删除是一个很危险的操作, 最好与用户进行二次确认
            choice = input('亲, 确定删除该学生数据吗? (y删除/n取消):')
            if choice.lower() == 'y':
                # 删除
                cls.stus.pop(stu_index)
                print('删除成功')
            else:

                print('取消删除操作')

        else:
            # 学号不存在
            print(f'没有该学号的学生数据, 无法删除')


if __name__ == '__main__':
    # main 方法中执行测试方法
    # 执行 StudentManager 类的show_menu方法
    StudentManager.show_menu()
