# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/18 23:47
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask

# 1.创建falsk app 对象
app = flask.Flask(__name__)


# 3.默认访问服务端的根路由
@app.route('/')
def index():
    html = '''
        <h1>Hello everyone</h1>
        <a href="/chinese">中文</a></br>
        <a href="https://www.baidu.com">百度</a>
    '''
    return html

# 其他路由
@app.route('/chinese')
def chinese():
    html = '''
        <h1>嗨, 大家好啊</h1>
        <a href="/">英文</a></br>
        <a href="https://www.baidu.com">百度</a>
        '''
    return html


# 2.启动app服务端对象
if __name__ == '__main__':
    app.run()
