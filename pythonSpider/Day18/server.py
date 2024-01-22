# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/12 20:08
@Auth ： 异世の阿银
@File ：server.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return flask.render_template('books.html')


# a 超链接标签,携带参数的get请求
@app.route('/<page_url>')
def go_url(page_url):
    return flask.render_template(page_url)


if __name__ == '__main__':
    app.run()