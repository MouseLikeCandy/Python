# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 18:59
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
模板语言--分支结构
'''
import flask
app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    name = '翠花'
    gender = 'M'
    age = 15
    return flask.render_template('show2.html', name=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run()