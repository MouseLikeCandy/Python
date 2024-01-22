# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/22 22:26
@Auth ： 异世の阿银
@File ：studentManagerServer.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 学生管理系统的服务端
# 定义一个数据库操作类（对MySQL数据库是西安增删改查）
'''
import flask



# 定义一个数据库操作类（对MySQL数据库实现增删改查）
class StudentDB(object):
    pass




app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 路由 + 逻辑处理
@app.route('/')
def index():
    # 取出客户端发送的opt行为参数(option 选项)
    opt = flask.request.values.get('opt', '')
    print(f'opt = {opt}')

    # 判断
    if opt == 'query':
        # 从数据库查询数据,然后将查询到的数据返回给客户端
        pass

    return f'opt = {opt}'


if __name__ == '__main__':
    app.run()