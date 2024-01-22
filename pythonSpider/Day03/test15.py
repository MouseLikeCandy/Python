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
        <form action='#' method='get'>
            user <input type="text" name='user'/><br/>
            pwd <input type='password' name='pwd'><br/>
            <input type='submit' value='提交'>
        </form>
    '''
    # 获取浏览器端发送给服务器端的数据信息(user,pwd)
    user = flask.request.values.get('user', '')
    pwd = flask.request.values.get('pwd', '')
    return html + f'你输入的数据为: user = {user}, pwd = {pwd}'
    return html + f'<div>你输入的数据为: user = {user}, pwd = {pwd}</div>'

# 2.启动app服务端对象
if __name__ == '__main__':
    app.run()

#  请求方式:
# 1. get 数据在url地址栏中直接拼接,数据不安全,可以直接被看见
# 使用场景: 不敏感的数据, 一般get请求方式都是获取的, get请求发送数据是有一定长度限制的.
