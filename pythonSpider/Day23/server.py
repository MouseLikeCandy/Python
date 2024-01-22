# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 18:11
@Auth ： 异世の阿银
@File ：server.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 根路由
@app.route('/')
def index():
    return flask.render_template('phone.html')

@app.route('/show')
def show():
    return 'Server Message'

if __name__ == '__main__':
    app.run()