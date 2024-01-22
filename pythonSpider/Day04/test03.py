# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 18:05
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
模板用户登录
'''
import flask

app = flask.Flask(__name__, static_folder="static", template_folder="templates")


# 路由 + 逻辑处理
# 根路由
@app.route('/', methods=['get', 'post'])
def index():
    if flask.request.method == 'POST':
        # 提交数据
        # 取数据
        user = flask.request.values.get('user')
        pwd = flask.request.values.get('pwd')
        # 判断
        if user == '张三' and pwd == '333':
            # 登陆成功
            msg = '登陆成功!'
        else:
            # 登陆失败
            msg = '用户名或密码错误!'
        print('POST请求...')
    else:
        # 获取数据
        msg = ''
        user = ''   # <!-- 记住用户名 -->
        print('GET请求...')
        # msg=msg, key=value
        # 登录失败, 用户名仍然显示
    return flask.render_template('show.html', msg=msg, user=user)  # <!-- 记住用户名 -->


if __name__ == '__main__':
    app.run()
