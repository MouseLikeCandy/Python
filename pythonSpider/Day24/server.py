# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/17 19:52
@Auth ： 异世の阿银
@File ：server.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import flask
app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    user = flask.request.values.get('user', '')
    pwd = flask.request.values.get('pwd', '')
    if user == 'xxx' and pwd == '123':
        return flask.redirect('/show')
    else:
        return flask.render_template('login.html')


@app.route('/show', methods=['GET', 'POST'])
def show():
    html = '''
    <table border='1'>
    <tr><td>品牌</td><td>型号</td><td>价格</td></tr>
    <tr><td>华为</td><td>P9</td><td>3800</td></tr>
    <tr><td>华为</td><td>P10</td><td>4200</td></tr>
    <tr><td>苹果</td><td>iPhone6</td><td>5800</td></tr>
    </table>
    <p>
    <a href='/'>退出</a>
    '''
    return html


if __name__ == '__main__':
    app.run()