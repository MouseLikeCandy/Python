# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 22:03
@Auth ： 异世の阿银
@File ：server1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 路由 + 逻辑处理
@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run()