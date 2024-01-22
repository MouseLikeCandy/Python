# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/3 19:46
@Auth ： 异世の阿银
@File ：server1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
上传服务器
'''
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 路由 + 逻辑处理
@app.route('/upload', methods=['get', 'post'])  # 405 Method not allowed
def upload():
    # 实现异常处理
    msg = ''
    try:
        # 获取上传文件的名称
        filename = flask.request.values.get('filename', '')
        # 如果客户端发送了filename值.就可以获取,但是也可能没有值
        # 为了保证客户端的判断准确性， 服务端也实现一次判断（双重保障）
        if filename:    # filename名称有值
            # 文件名称是存在的，接下来就需要获取客户端发送而来的二进制数据
            data = flask.request.get_data()  # get_data()来获取上传的二进制数据
            # 保存二进制数据
            with open(filename, 'wb') as f:
                f.write(data)
            # 给客户端回送一个信息
            msg = 'OK'
        # else:
        #     msg = ''
    except BaseException as e:  # 排除异常
        # 处理异常情况
        msg = str(e)    # e是一个BaseException 类型的异常对象, 最好将对象转换为str类型返回

    # 返回 msg 消息
    return msg  # 在请求响应模型中,不管返回的是什么,服务端会把信息直接包装成响应对象 http response对象


if __name__ == '__main__':
    app.run()