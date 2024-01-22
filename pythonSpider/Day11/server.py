# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/10 10:59
@Auth ： 异世の阿银
@File ：server.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask

import mysql.connector

class StudentDB(object):
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

    # 根据学号查询数据库中是否存在该学生的信息
    def select_by_id(self, stu_id):
        res = {}
        try:
            sql = 'select * from students where stu_id = %s;'
            values = (stu_id, )
            self.cursor.execute(sql, values)
            # 如果这个查询成功,也仅能查询到一条数据
            row = self.cursor.fetchone()    # 一行数据
            print(f'row = {row}')
            # 封装为字典
            stu_dict = {}
            stu_dict['stu_id'] = row[0]
            stu_dict['name'] = row[1]
            stu_dict['age'] = row[2]
            stu_dict['score'] = row[3]
            res['data'] = stu_dict

            res['msg'] = 'OK'
        except BaseException as e:
            res['msg'] = str(e)
        return res

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
db = StudentDB()

# 说明: 访问根路由直接返回index.HTML 首页页面
@app.route('/')
def index():
    return flask.render_template('index.html')


# <> 表示路由中有一个参数, 可以用<参数名称>
@app.route('/<page_url>', methods=['GET', 'POST'])
def go_page(page_url):
    opt = ''
    print(f'page_url={page_url}')   # page_url=query.html ->逻辑就是查询
    # page_url是一个字符串类型的数据, 字符串类型的数据有一个endswith()方法, 可以判断字符串以什么结尾.
    if page_url.endswith('.html'):
        # 取出.html之前的内容
        # opt = page_url.split('.')[0]
        opt = page_url[:-5]     # 切片, 从头开始切, 最后5个字符不需要
    else:
        # 表单发送的请求没有后缀.html
        # 例如: 添加页面发送的/add post请求
        opt = page_url

    # 此处需要进行请求类型判断
    if flask.request.method == 'POST':
        # 提交数据
        if opt == 'add':
            print('--添加--')
            # 获取浏览器提交过来的所有数据
            stu_id = flask.request.values.get('stu_id', '')
            name = flask.request.values.get('name', '')
            age = flask.request.values.get('age', '')
            score = flask.request.values.get('score', '')
            res = db.insert_row(stu_id, name, int(age), float(score))
            if res['msg'] == 'OK':
                # 添加成功, 跳转到查询页面
                # 如果程序通过render_template跳转到其他页面, 不会发请求导致没有数据
                # 解决方案: 让页面进行 重定向 , 重新发送请求 get请求
                # return flask.render_template('query.html', res=res)
                return flask.redirect('/query.html')
            else:
                # 添加失败, 返回首页
                # return flask.redirect('/index.html', res=res)
                return flask.render_template('index.html', res=res)
        elif opt == 'delete':
            stu_id = flask.request.values.get('stu_id', '')
            # 真实删除
            res = db.delete_row(stu_id)
            if res['msg'] == 'OK':
                return flask.redirect('/query.html')
            else:
                return flask.render_template('index.html', res='删除学生信息失败!')
        elif opt == 'update':
            print('--更新--')
            # 获取浏览器提交过来的所有数据
            stu_id = flask.request.values.get('stu_id', '')
            name = flask.request.values.get('name', '')
            age = flask.request.values.get('age', '')
            score = flask.request.values.get('score', '')
            res = db.update_row(stu_id, name, int(age), float(score))
            if res['msg'] == 'OK':
                return flask.redirect('/query.html')
            else:
                return flask.render_template('index.html', res='更新学生信息失败!')
        else:
            res = {}
    else:
        # 查询数据

        if opt == 'query':
            print('--查询--')
            res = db.select_rows()
        elif opt == 'update':
            print('--修改--')
            # 需要获取stu_id
            stu_id = flask.request.values.get('stu_id', '')
            res = db.select_by_id(stu_id)
        elif opt == 'delete':
            print('--删除--')
            stu_id = flask.request.values.get('stu_id', '')
            res = db.select_by_id(stu_id)
        else:
            res = {}

    # 页面不仅需要实现跳转, 同时需要将数据传递给该页面, res 参数表示数据额
    return flask.render_template(page_url, res=res)


if __name__ == '__main__':
    app.run()



# jinja2.exceptions.TemplateNotFound: favicon.ico  网站图标