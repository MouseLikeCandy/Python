# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/10 6:56
@Auth ： 异世の阿银
@File ：server2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
浏览器下载, 客户端就是浏览器 
'''
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

# 浏览器发送的请求 url ='http://127.0.0.1:5000/download?filename=1.JPG'
@app.route('/download', methods=['post', 'get'])
def download():
    # 下载固定文件
    filename = 'static/1.jpg'
    with open(filename, 'rb') as f:
        data = f.read()
    # return data # 浏览器中显示图片的乱码

    # http协议规定， 浏览器下载需要设置的一些字段名称  服务端需要设置响应头部信息
    response = flask.make_response(data)
    response.headers['content-type'] = 'application/octet-stream'
    # content-disposition 内部部署  attachment 附件
    response.headers['content-disposition'] = 'attachment;filename=1.jpg'
    return response     # 返回响应对象

if __name__ == '__main__':
    app.run()
