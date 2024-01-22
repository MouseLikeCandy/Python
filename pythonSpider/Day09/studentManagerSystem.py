# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/22 22:25
@Auth ： 异世の阿银
@File ：studentManagerSystem.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import urllib.request
import sys
import json
import urllib.parse
'''
基于WEB的学生管理系统 V4
思路： 原来数据存储在文件中, 现在数据要存储到数据库中
区别： 文件数据的存储是由客户端自己决定的，但是数据库中数据的存储是交给服务端来实现的，所以客户端不需要考虑文件怎么存；

建立一个opt的参数表
opt值        含义
init        初始化学生表
insert      增加学生
delete      删除学生
update      修改学生
query       获取学生记录
发送: opt='init'
返回: {'msg': 'OK'}

JSON
# 说明: 在网路上传输数据时,不能以字典的形式传输,而需要将字典格式转换为json数据类型的字符串格式才能实现传输.
# 什么是JSON
1. JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式.
2. JSON 采用完全独立于语言的文本格式来存储和表示数据. 简洁和清晰的层次结构使得 JSON 成为理想的数据交互
语言, 易于阅读和编写, 同时也易于机器解析和生成, 并有效地提升网络传输效率.
3. JSON 在 Python 中分别由 dict 和 list 组成. {key1: value1, key2: […]   字典嵌套列表
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

    # 为了能够使用sort方法,Student类要重写object类的lt方法. 完成自定义对象的排序规则定义.
    # 层序底层90%不适用冒泡排序  ON的效率, 效率太低
    def __lt__(self, other):
        return self.score < other.score

# 2. 定义一个学生管理类(数据库存储)
class StudentManager(object):
    # 定义一个stus列表存储学生数据
    stus = []
    # 定义一个stus文件
    # filename = 'stus.txt'
    # 思路： 原来数据存储在文件中, 现在数据要存储到数据库中
    # 区别： 文件数据的存储是由客户端自己决定的，但是数据库中数据的存储是交给服务端来实现的，所以客户端不需要考虑文件怎么存；
    url = 'http://127.0.0.1:5000'

    @classmethod
    def init_db(cls):
        # opt=init 参数名称
        try:
            response = urllib.request.urlopen(cls.url + '?opt=init')
            json_str = response.read().decode()
            res = json.loads(json_str)
            msg = res['msg']
            if msg == 'OK':
                print('数据库连接初始化成功!')
            else:
                print(msg)
        except BaseException as e:
            print(e)

    # 应该告诉服务端，客户端需要读数据库中的所有数据
    @classmethod
    def read_data(cls):
        # 思路： 客户端发送查询的请求给服务端
        # 说明： 请求发送可能会失败，原因有很多，比如服务端未启动。。。
        try:
            # 发送请求，接收响应
            response = urllib.request.urlopen(cls.url + '?opt=query')
            # 思考: 请求发送成功后, 可以得到一个response对象, response对象中有所有对象的数据.

            # 需求: 取出data中的数据
            # res 是一个字符串str类型的数据
            res = response.read().decode()
            print(f'{type(res)}: {res}')
            # string indices must be integers 字符串取数据必须使用下标. 因为字符串中使用下标可以取出字符串中对应的字符.
            # data = res['data']  # 这个方式是字典取数据的行为.
            # print(data)
            # 思考: 有没有方法将字符串类型的数据转为字典类型数据?
            # 说明: 在网路上传输数据时,不能以字典的形式传输,而需要将字典格式转换为json数据类型的字符串格式才能实现传输.
            res = json.loads(res)   # json.loads()方法可以将json数据类型的字符串转换为Python语言中的字典类型.

            msg = res['msg']
            if msg == 'OK':
                data = res['data']
                print(f'{type(res)}: {res}')
                print(type(data), data)

                # 遍历data列表
                for stu_dict in data:
                    stu_id = stu_dict['stu_id']
                    name = stu_dict['name']
                    age = stu_dict['age']
                    score = stu_dict['score']
                    # 将获取的数据封装为Student类型的对象
                    stu = Student(stu_id, name, age, score)
                    # 将stu存储到stus列表中
                    cls.stus.append(stu)
            else:
                print(msg)

        except BaseException as e:
            print(e)

    # 定义一个关闭连接对象的方法
    @classmethod
    def close(cls):
        try:
            response = urllib.request.urlopen(cls.url + '?opt=quit')
            json_str = response.read().decode()
            res = json.loads(json_str)
            msg = res['msg']
            if msg == 'OK':
                print('成功关闭数据库连接对象!')
            else:
                print(msg)
        except BaseException as e:
            print(e)

    # 静态方法, 没有访问类数据
    @staticmethod
    def show_menu():
        # 发送一个初始化db对象的请求
        StudentManager.init_db()
        # 读取文件中的数据到程序里
        StudentManager.read_data()
        while True:
            # 1. 界面展示
            menu = '''
            ----- 欢迎来到学生管理系统 V 3.0-----
                1.查看所有学生
                2.添加学生
                3.修改学生
                4.删除学生
                5.排序学生
                6.退出程序
            '''
            print(menu)
            # 2. 提示用户输入操作码
            choice = input('亲, 请输入执行的操作码: ')
            # 3. 用户操作码的判断
            if choice == '1':
                # 查看所有学生
                StudentManager.query_students()  # query_students是一个类方法: 类名.类方法
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
                # 排序学生
                StudentManager.sort_students()
            elif choice == '6':
                # 退出程序

                # 需要向服务端发送一个关闭'数据库连接对象'的请求.
                StudentManager.close()
                print('感谢您的使用,下次再会!')
                sys.exit()
                # break
            else:
                # 操作码不在指定范围内,提示错误
                print('亲, 操作码错误,请重新输入操作码')



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

        # 说明: 数据应该先完成数据库的存储, 然后再将数据存储到程序的列表中.要让数据库中的数据与程序列表中的数据保持同步.
        try:
            # 发送请求
            # 封装需要传递给服务器的学生数据  quote 引用汉字
            data = f'stu_id={stu_id}&name={urllib.parse.quote(name)}&age={age}&score={score}'
            # post请求要求使用字节数据传递
            data = data.encode()
            response = urllib.request.urlopen(cls.url + '?opt=insert', data)   # 学生数据使用post请求传递
            # 取出response对象的数据
            json_res = response.read().decode()
            # 将json格式的字符串类型转为python语言的字典类型数据
            res = json.loads(json_res)
            # 取出字典中的msg信息
            msg = res['msg']
            if msg == 'OK':
                # 数据库中插入数据成功
                # 3. 将用户输入的数据包装为学生对象
                # 学生信息对象格式
                stu = Student(stu_id, name, age, score)
                cls.stus.append(stu)
                print(f'添加成功')
            else:
                # 数据库插入数据失败
                print(msg)
        except BaseException as e:
            print(e)



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
                print('该学号的学生存在')
                break
            else:
                # 学号不存在
                flag = False
        else:
            print(f'没有该学号的学生数据')

        # 4. 提示用户输入该学号对应学生的新的name, age, score
        if flag:
            # 输出已存在的学生信息
            print(cls.stus[stu_index])
            # 提示修改
            name = input('亲, 请输入学生新的姓名:')
            age = input('亲, 请输入学生新的年龄:')
            score = input('亲, 请输入学生新的成绩:')

            # 发送请求, 并传递数据 opt=update
            # 先要保证数据库中的数据是准确的, 然后再同步程序中的列表数据
            try:
                data = f'stu_id={stu_id}&name={urllib.parse.quote(name)}&age={age}&score={score}'
                data = data.encode()
                response = urllib.request.urlopen(cls.url + '?opt=update', data)  # 学生数据使用post请求传递
                json_res = response.read().decode()
                res = json.loads(json_res)
                msg = res['msg']
                if msg == 'OK':
                    # 包装新数据
                    new_stu = Student(stu_id, name, age, score)
                    # 替代 stus 列表中原来对应的数据
                    cls.stus[stu_index] = new_stu
                    print(f'修改成功')
                else:
                    # 数据库修改数据失败
                    print(msg)
            except BaseException as e:
                print(e)

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

                # 首先删除数据库中对应该学生数据
                try:
                    # 发送请求, 传递stu_id给服务端, opt=delete
                    # data=stu_id.encode() 说明: 关键字传参, data=post数据,post数据必须为'字节数据',所以stu_id.encode() 方法实现类型转换
                    response = urllib.request.urlopen(cls.url + '?opt=delete', data=f'stu_id={stu_id}'.encode())
                    json_str = response.read().decode()
                    res = json.loads(json_str)
                    msg = res['msg']
                    if msg == 'OK':
                        # 再同步删除列表中的数据
                        cls.stus.pop(stu_index)     # 推荐使用
                        # del stus[stu_index]

                        print('删除成功')
                    else:
                        # 数据库删除数据失败
                        print(msg)
                except BaseException as e:
                    print(e)

            else:
                print('取消删除操作')

        else:
            # 学号不存在
            print(f'没有该学号的学生数据, 无法删除')
    # 5. 排序学生
    @classmethod
    def sort_students(cls):
        # 排序
        # TypeError: '<' not supported between instances of 'Student' and 'Student'
        # 类型错误: 在学生对象和学生对象之间不支持'小于'操作的操作.
        # sort()会自动调用学生对象的 < 操作符.
        # 问题: 学生对象没有定义比较的规则.
        # 如何告诉sort排序方法, 学生对象使用'成绩'作为比较规则.
        # 方案: sort 方法会自动调用学生对象的 < 操作符.  __lt__方法  less than
        cls.stus.sort(reverse=True)
        cls.query_students()

if __name__ == '__main__':
    # main 方法中执行测试方法
    # 执行 StudentManager 类的show_menu方法
    StudentManager.show_menu()