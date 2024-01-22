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
# 说明: 在浏览器使用http://127.0.0.1:5000/访问服务端, 这种访问方式属于get请求
@app.route('/')
# @app.route('/', methods=['get', 'post'])
def index():
    html = '''
        <form action='#' method='post'>
            user <input type="text" name='user'/><br/>
            pwd <input type='password' name='pwd'><br/>
            <input type='submit' value='提交'>
        </form>
    '''
    # 获取浏览器端发送给服务器端的数据信息(user,pwd)
    user = flask.request.values.get('user', '')     # 数据在form data中
    pwd = flask.request.values.get('pwd', '')
    return html + f'你输入的数据为: user = {user}, pwd = {pwd}'


# 2.启动app服务端对象
if __name__ == '__main__':
    app.run()

#  请求方式:
# 1. get 数据在url地址栏中直接拼接,数据不安全,可以直接被看见
# 使用场景: 不敏感的数据, 一般get请求方式都是获取的, get请求发送数据是有一定长度限制的.
# 三种get请求:①浏览器直接访问②a标签超链接③img标签访问图片


# 2. post 数据在表单'formdata'中, 不显示在浏览器的url上, 数据较为安全.  加密后更安全
# 使用场景: 敏感数据,post请求没有长度的限制.
