# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/22 22:26
@Auth ： 异世の阿银
@File ：studentManagerServer.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import json

'''
# 学生管理系统的服务端
# 定义一个数据库操作类（对MySQL数据库是西安增删改查）
'''
'''
服务端可以接收多个客户端的连接, 但是每个客户端都应该拥有一个独立的连接对象.
如果db数据库对象是全局变量的话, 意味着所有的客户端使用的都是同一个连接对象.
'''
import flask
import mysql.connector


# 定义一个数据库操作类（对MySQL数据库实现增删改查）
class StudentDB(object):
    # 定义一个'类变量', 默认值为空对象
    db = None

    # 初始化db类数据
    @classmethod
    def init_db(cls):
        try:
            cls.db = StudentDB()
            res = {'msg': 'OK'}
        except BaseException as e:
            res = {'msg': str(e)}

    # 关闭数据库连接对象
    def close_db(self):
        try:
            self.cursor.close()
            self.conn.close()
            res = {'msg': 'OK'}
        except BaseException as e:
            res = {'msg': str(e)}
        return res

    # 数据库的初始化操作, 主要完成数据库和数据表的创建
    def __init__(self):
        # 1. 获取MySQL数据库服务的连接
        self.conn = mysql.connector.connect(host='localhost', user='root', password='123456',
                                            auth_plugin='mysql_native_password')
        # 2. 获取连接对象的'游标'对象
        self.cursor = self.conn.cursor()
        # 3. 执行sql语句,创建一个数据库
        # IF NOT EXISTS 如果这个数据库不存在,就创建,已经存在就不会创建.
        sql_db = 'create database IF NOT EXISTS student_db;'
        self.cursor.execute(sql_db)
        # 4. 指定连接对象执行的数据库(切换了数据库)
        self.cursor.execute('use student_db;')
        # 5. 创建数据表 对应数据模型Student类 def __init__(self, stu_id, name, age, score):
        sql_table = '''
            create table IF NOT EXISTS students(
                stu_id varchar(8) primary key,
                name varchar(16),
                age int,
                score float
            );
        '''
        self.cursor.execute(sql_table)

    # 查询数据库中的所有数据
    def select_rows(self):
        # 定义一个空字典, 返回给客户端的数据
        res = {}
        # 定义一个列表, 存储多个student数据
        data = []

        try:
            # 1. 定义查询语句
            sql = 'select * from students;'
            # 2. 执行查询语句
            self.cursor.execute(sql)
            # 3. 获取查询的所有结果集
            result_set = self.cursor.fetchall()  # result_set是一个列表类型的结果集
            # 4. 遍历 result_set 列表
            for row in result_set:
                print(row)  # row 是元组数据类型, 一个元组类型对应一个学生数据
                # 定义一个空字典
                stu_dict = {}
                stu_dict['stu_id'] = row[0]
                stu_dict['name'] = row[1]
                stu_dict['age'] = row[2]
                stu_dict['score'] = row[3]
                data.append(stu_dict)

            # 设置字典的key与value
            res['data'] = data
            res['msg'] = 'OK'
        except BaseException as e:
            res['msg'] = str(e)  # 将异常对象转换为了字符串类型的数据

        return res  # 返回一个数据封装完成的字典

    # 将数据插入到数据库中
    def insert_row(self, stu_id, name, age, score):
        res = {}
        try:
            sql = 'insert into students(stu_id, name, age, score) values(%s, %s, %s, %s);'
            values = (stu_id, name, age, score)
            self.cursor.execute(sql, values)
            # 一定要提交数据, 否则数据不发生任何更改, 但是程序不会报错
            self.conn.commit()
            res['msg'] = 'OK'
        except BaseException as e:
            res['msg'] = str(e)

        return res

    # 修改数据库中的数据
    def update_row(self, stu_id, name, age, score):
        print('--修改学生信息--')
        res = {}
        try:
            sql = 'update students set name = %s, age = %s, score = %s where stu_id = %s;'
            values = (name, age, score, stu_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
            res['msg'] = 'OK'
            print('--修改学生信息完成--')
        except BaseException as e:
            res['msg'] = str(e)

        return res

    # 删除数据库中对应学号的学生数据
    def delete_row(self, stu_id):
        print('--删除学生数据--')
        # stu_id 可能为空字符串导致向下执行没有语法错误, 但不成功
        try:
            sql = 'delete from students where stu_id = %s;'
            # values = (stu_id, )
            # self.cursor.execute(sql, values)
            # params=(stu_id, ) 参数数据的关键字名称叫做params 是元组类型
            # self.cursor.execute(operation=sql, params=(stu_id, ))   # 关键字参数
            self.cursor.execute(sql, (stu_id,))     # 位置参数
            # 提交数据
            self.conn.commit()
            res = {'msg': 'OK'}
        except BaseException as e:
            res = {'msg': str(e)}

        return res


# app和db都是全局变量,服务端一启动,这两个对象就会被创建
app = flask.Flask(__name__, static_folder='static', template_folder='templates')
# 定义一个全局的StudentDB对象, 主要用来完成数据库中数据的'增删改查'功能.
# db = StudentDB()  # 思考: StudentDB()这句代码调用了什么方法? 调用了StudentDB类的__init()__方法.
# 一旦将db数据库对象定义为了StudentDB的类数据, 之前的db全局变量使用处就会报错.


# 路由 + 逻辑处理
@app.route('/', methods=['GET', 'POST'])
def index():
    # 取出客户端发送的opt行为参数(option 选项)
    opt = flask.request.values.get('opt', '')
    print(f'opt = {opt}')

    # 判断
    # opt => query, insert, update, delete ....
    # 1. 定义一个字典

    if opt == 'query':
        # 从数据库查询数据,然后将查询到的数据返回给客户端
        # json格式的数据,其实是字符串类型的数据,但是这个字符串中的格式类似于python中的字典格式.
        # json格式的数据,字符串key不可以使用单引号,因为在很多语言中,单引号仅仅表示一个字符,而不是字符串.
        # 实现: 将一个python类型的字典数据,直接转换为了'字符串类型'的数据.
        # 分析: 1.服务端能不能直接返回一个'字典类型'的数据给客户端?  可以返回给客户端, 但是客户端接收的数据类型为 字符串类型
        # 分析: 2.如果服务端返回的是字符串类型的数据, 客户端接收的同样还是字符串的数据.
        # res = '{"msg": "OK", "data": [{"stu_id": "1001", "name": "张三", "age": 18, "score": 88}, {"stu_id": "1002", "name": "李四", "age": 19, "score": 99}]}'
        # 没有最外侧的单引号, 但在传输时也会自动封装为字符串
        # res = {"msg": "OK", "data": [{"stu_id": "1001", "name": "张三", "age": 18, "score": 88}, {"stu_id": "1002", "name": "李四", "age": 19, "score": 99}]}
        # json数据中不能使用单引号
        # res = '{"msg": "OK", \'data\': [{"stu_id": "1001", "name": "张三", "age": 18, "score": 88}, {"stu_id": "1002", "name": "李四", "age": 19, "score": 99}]}'

        # 需求: 需要将一个字典类型的数据转换为json格式的字符串类型的数据.
        # res['msg'] = 'OK'
        # res['data'] = [{'stu_id': '1001', 'name': '张三', 'age': 18, 'score': 88}, {'stu_id': '1002', 'name': '李四', 'age': 19, 'score': 99}]
        #
        # print('转换前', type(res), res)

        # 数据从数据库中来
        # 调用数据库的查询数据行为
        res = StudentDB.db.select_rows()

    elif opt == 'insert':
        # 获取客户端传送过来的学生数据(stu_id, name, age, score)
        stu_id = flask.request.values.get('stu_id', '')
        name = flask.request.values.get('name', '')
        age = flask.request.values.get('age', '')
        score = flask.request.values.get('score', '')
        # 使用数据库对象, 将数据存储到数据库中
        res = StudentDB.db.insert_row(stu_id, name, int(age), float(score))
    elif opt == 'update':
        # 获取客户端传递来的数据, 调用数据库对象执行更新数据行为.
        stu_id = flask.request.values.get('stu_id', '')
        name = flask.request.values.get('name', '')
        age = flask.request.values.get('age', '')
        score = flask.request.values.get('score', '')
        # 使用数据库对象, 将数据存储到数据库中
        res = StudentDB.db.update_row(stu_id, name, int(age), float(score))
    elif opt == 'delete':
        # 获取客户端传递来的stu_id参数,同时调用数据库对象执行删除该学号的学生信息.
        stu_id = flask.request.values.get('stu_id', '')
        res = StudentDB.db.delete_row(stu_id)
    elif opt == 'init':
        # 初始化db对象
        # 类数据使用类方法来实现数据初始化
        # 注意: 在执行StudentDB.init_db()之前, db对象是一个None对象.
        res = StudentDB.init_db()     # init_db()是一个类方法, 所以需要使用类名来调用
    elif opt == 'quit':
        # 需要关闭数据库连接对象
        res = StudentDB.db.close_db()
    else:
        # 兜底语句
        res = {'msg': 'failure'}

    # 返回之前进行格式转换 python字典->json字符串
    res = json.dumps(res)
    print('转换后', type(res), res)
    return res


if __name__ == '__main__':
    app.run()
