# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 17:50
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
目录结构划分:
static: 静态资源文件
templates: 网页文件

请求方式--从客户端到服务端
模板语言--从服务端到客户端
'''

import flask

# 1.创建app对象
# 参数传递问题: 如果一个关键字参数有默认值, 可以不传递. 写出来阅读性更高.
# app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app = flask.Flask(__name__)


# 3. 路由 + 逻辑控制
@app.route('/')
def index():
    # 需求: 直接返回'静态模板'页面
    return flask.render_template('qiangjinjiu.html')  # 渲染模板, 渲染一个静态页面


# 2.启动app对象
if __name__ == '__main__':
    app.run()


# "GET / HTTP/1.1" 200 -  200 访问成功
# "GET /static/1.jpg HTTP/1.1" 304 -  304 静态资源缓存,第二次访问

