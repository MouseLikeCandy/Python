# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 18:59
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
模板语言--循环
'''
import flask
app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    students = []
    stu1 = {'name': '张三', 'age': 18, 'gender': '男'}
    stu2 = {'name': '李四', 'age': 17, 'gender': '女'}
    stu3 = {'name': '王五', 'age': 19, 'gender': '男'}
    students.extend([stu1, stu2, stu3])
    return flask.render_template('show3.html', stus=students)


if __name__ == '__main__':
    app.run()