# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/12 21:18
@Auth ： 异世の阿银
@File ：server.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
防止爬网站时被封, 先爬取自己的
'''

import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return flask.render_template('test.html')


if __name__ == '__main__':
    app.run()