# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/28 7:01
@Auth ： 异世の阿银
@File ：server2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''GET POST 方法传递数据的混合使用'''
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 路由 + 逻辑处理
@app.route('/', methods=['get', 'post'])
def index():
    # 解析客户端传送过来的数据
    province = flask.request.values.get('province', '')
    city = flask.request.values.get('city', '')
    note = flask.request.values.get('note', '')
    # 返回数据, 虽然这里看起来是一个字符串, 但这里是请求响应模型, 所有的数据都会被包装到响应对象中, 最后返回.
    return province + ',' + city + ',' + note

if __name__ == '__main__':
    app.run()