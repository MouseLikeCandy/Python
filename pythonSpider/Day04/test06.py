# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 18:59
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
电影榜单数据显示
'''
import flask
app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    # 定义一个电影列表
    movies = []
    # 定义一个序号
    number = 1
    # 读取文件中的数据, csv文件, 就是使用'逗号'分隔数据的文件
    with open('static/movie_Top250.csv', mode='rt', encoding='utf-8') as f:
        # 按行读取数据
        for line in f.readlines():
            line = line.strip()  # 处理每一行中最后的换行符\n
            # 切割数据
            datas = line.split(',')
            title = datas[0]
            star = datas[1]
            quote = datas[2]
            detail_url = datas[3]
            print(f'title = {title}, star = {star}, quote = {quote}, detail_url = {detail_url}')

            # 将数据封装为一个字典
            movie = {'number': number, 'title': title, 'star': star, 'quote': quote, 'detail_url': detail_url}
            # 将封装完毕的字典数据存储到电影列表中
            movies.append(movie)
            number += 1
    return flask.render_template('show4.html', movies=movies)


if __name__ == '__main__':
    app.run()