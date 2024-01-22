# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/10 6:56
@Auth ： 异世の阿银
@File ：server2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import urllib.parse
import flask
import os
'''
上传与下载合并
'''

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ''
    if flask.request.method == 'POST':
        # 浏览器上传: （从浏览器）先读（一个文件）后写（进入服务器）
        file = flask.request.files['upload_file']
        if file:
            # 文件存在
            data = file.read()
            with open('static/' + file.filename, 'wb') as f:
                f.write(data)
            # 提示信息
            msg = f'文件上传成功！'
        else:
            # 文件不存在
            msg = '请选择需要上传的文件！'
    else:
        # 浏览器下载：（从服务器）先读（给浏览器）后写（一个文件）

        filename = flask.request.values.get('filename', '')
        print(f'filename = {filename}')

        # 判断
        if filename:
            # 文件存在
            with open('static/' + filename, 'rb') as f:
                data = f.read()
            # http协议有规定
            response = flask.make_response(data)
            response.headers['content-type'] = 'application/octet-stream'
            response.headers['content-disposition'] = 'attachment;filename=' + urllib.parse.quote(filename)
            return response

    files = os.listdir('static')
    return flask.render_template('upload.html', files=files, msg=msg)


if __name__ == '__main__':
    app.run()
