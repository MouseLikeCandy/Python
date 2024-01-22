# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/20 13:05
@Auth ： 异世の阿银
@File ：server3.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask
import json
import time


app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('phone2.html')


@app.route('/marks')
def loadMarks():
    time.sleep(1)   # 模拟延时, 这1秒钟是拿不到数据的
    marks = ['华为', '苹果', '三星']
    return json.dumps(marks)


if __name__ == '__main__':
    app.run()