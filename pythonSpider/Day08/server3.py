# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/10 6:56
@Auth ： 异世の阿银
@File ：server2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
浏览器表单上传, 客户端就是浏览器
'''
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['post', 'get'])
def index():
    if flask.request.method == 'POST':
        # post请求, 上传资源
        file = flask.request.files['upload_file']  # 不是从values中取, 而是从files中取
        # print(f'file = {file}')
        if file:
            # 文件存在
            data = file.read()  # 直接获取文件对象中存储的二进制数据
            with open('static/' + file.filename, 'wb') as f:
                f.write(data)
            msg = f'文件上传成功! {file.filename}, 字节数: {len(data)}'
        else:
            # 文件不存在
            msg = '文件不存在, 上传失败!'
        return msg
    else:
        # get请求, 浏览器直接访问的请求类型是get请求

        return flask.render_template('form.html')


if __name__ == '__main__':
    app.run()
