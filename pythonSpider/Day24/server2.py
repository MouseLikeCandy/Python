# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 20:24
@Auth ： 异世の阿银
@File ：server2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
selenium 爬取 Ajax 请求

Ajax 异步刷新: 说明: 当我们操作品牌时, 页面的url并未发生更改, 但是数据却实现了局部的刷新.
现在网页中大量使用了Ajax技术, 通过 JavaScript 在客户端向服务器发出请求, 服务器返回数据给客户端, 客户端再把数据展现出来, 
这样做可以减少网页的闪动, 让用户有更好的体验.
'''
import flask
import json


app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('phone.html')


@app.route('/phones', methods=['GET', 'POST'])
def getPhones():
    mark = flask.request.values.get('mark', '')
    phones = []
    if mark == '华为':
        phones.append({'model': 'p9', 'mark': '华为', 'price': 3800})
        phones.append({'model': 'p10', 'mark': '华为', 'price': 4000})
    elif mark == '苹果':
        phones.append({'model': 'iPhone5', 'mark': '苹果', 'price': 5800})
        phones.append({'model': 'iPhone6', 'mark': '苹果', 'price': 6800})
    elif mark == '三星':
        phones.append({'model': 'Galaxy A9', 'price': 2800})
    return json.dumps({'phones': phones})


if __name__ == '__main__':
    app.run()