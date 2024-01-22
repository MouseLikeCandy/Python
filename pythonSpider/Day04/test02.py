# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 18:05
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask

app = flask.Flask(__name__, static_folder="static", template_folder="templates")


# 路由 + 逻辑处理
# 根路由
@app.route('/')
def index():
    return flask.render_template('login.html')


# 登录的路由地址
@app.route('/login', methods=['get', 'post'])  # 路由: 默认只接收get请求, 发post报405
def login():
    # 取出表单的提交数据
    # 请求响应模型
    # 客户端的所有数据在请求对象当中, 请求对象在flask框架之中
    user = flask.request.values.get('user')
    pwd = flask.request.values.get('pwd')
    html = f'user = {user}, pwd = {pwd}'
    return html


if __name__ == '__main__':
    app.run()
