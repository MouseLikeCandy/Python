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
# 浏览器端给服务器端传送数据有两种方式: get和post
# get传送的方式:http://127.0.0.1:5000/?key1=value&key2=value2&key3=value3
# get请求的数据会在url请求地址中直接显示
@app.route('/')
def index():
    # 获取浏览器端发送给服务器端的数据信息(user / pwd), 信息在请求对象中.
    user = flask.request.values.get('user', '默认用户')
    # 使用user作为key从请求中获取数据,如果没有user这个key, 则默认数据为空字符串(默认数据)
    pwd = flask.request.values.get('pwd', '默认密码')
    return f'你输入的数据为: user = {user}, pwd = {pwd}'


# 2.启动app服务端对象
if __name__ == '__main__':
    app.run()

# 访问
# http://127.0.0.1:5000
# http://127.0.0.1:5000/?user=张三&pwd=123456
