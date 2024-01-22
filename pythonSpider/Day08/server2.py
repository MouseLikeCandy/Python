# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/10 6:56
@Auth ： 异世の阿银
@File ：server2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
下载服务器
下载: 先读后写
'''
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    if 'filename' not in flask.request.values:  # values是一个列表数据
        # 如果请求中没有filename的key,服务端就会返回资源列表给客户端
        return f'[图片资源: 1.JPG, 2.JPG, 3.JPG]'
    else:
        # 请求中携带了filename的key,说明客户端需要下载资源
        filename = flask.request.values.get('filename', '')
        # 服务端: 读数据
        with open('static/' + filename, 'rb') as f:
            data = f.read()
        # return f'下载资源: {filename}'
        return data


if __name__ == '__main__':
    app.run()
