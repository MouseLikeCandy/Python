# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/24 20:11
@Auth ： 异世の阿银
@File ：server1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 预定义标签不是数据, 而是给浏览器排版用的
# 真正的数据是在页面中展示出来的.
# 浏览器自动解析了html
'''
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 路由+逻辑处理
@app.route('/')
def index():
    return flask.render_template('test3.html')


if __name__ == '__main__':
    app.run()
