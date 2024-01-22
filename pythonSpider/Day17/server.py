# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/8 12:19
@Auth ： 异世の阿银
@File ：server.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask
import os

app = flask.Flask(__name__, static_folder='static')


# 路由 + 逻辑处理
# http://127.0.0.1:5000/download?filename=1.jpg
@app.route('/download', methods=['get', 'post'])
def download():
    # 获取文件名称
    filename = flask.request.values.get('filename', '')
    # 判断文件名称是否存在
    if filename != '' and os.path.exists('static/' + filename):
        # 文件存在, 读取文件, 返回数据
        with open('static/' + filename, mode='rb') as f:
            data = f.read()
    else:
        # 文件不存在, 执行一些默认处理, 比如跳转..
        pass
    return data


if __name__ == '__main__':
    app.run()