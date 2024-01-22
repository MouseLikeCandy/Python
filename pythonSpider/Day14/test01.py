# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 6:40
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import urllib.request
import bs4
import mysql.connector
from bs4 import BeautifulSoup


# 创建一个University数据模型类
class University(object):
    # 初始化方法 ranking排行榜
    def __init__(self, ranking, university_name, province, typing, score, education_level):
        self.ranking = ranking
        self.university_name = university_name
        self.province = province
        self.typing = typing
        self.score = score
        self.education_level = education_level

    # 重写str方法
    def __str__(self):
        return f'University[ranking = {self.ranking}, university_name = {self.university_name}, ' \
               f'province = {self.province}, typing = {self.typing}, score = {self.score}, ' \
               f'education_level = {self.education_level}]'


# 创建一个数据库类
class UniversityDB(object):
    # 初始化数据(创建数据库和数据表)
    def __init__(self):
        sql_db = 'create database IF NOT EXISTS university_db;'
        # 创建一个数据库连接对象
        self.conn = mysql.connector.connect(host='127.0.0.1', user='root', password='123456', auth_plugin='mysql_native_password')
        # 获取对应的游标对象
        self.cursor = self.conn.cursor()
        # 执行创建数据库的sql
        self.cursor.execute(sql_db)
        # 切换数据库
        self.cursor.execute('use university_db;')
        # 创建数据表     varchar(8)  8是一个字节
        sql_table = '''
            create table university(
                ranking varchar(8), 
                university_name varchar(16) unique, 
                province varchar(8), 
                typing varchar(8), 
                score varchar(8), 
                education_level varchar(8)
            );
        '''
        try:
            self.cursor.execute(sql_table)
        except BaseException as e:
            # 表已经存在, 删除表中的旧数据
            print('表已经存在, 需要删除表中的所有数据! ')
            self.cursor.execute('delete from university')

    # 插入数据
    def insert_row(self, university):
        # 编写插入数据的sql语句
        sql = 'insert into university(ranking, university_name, province, typing, score, education_level)' \
              'values(%s, %s, %s, %s, %s, %s);'
        values = (university.ranking, university.university_name, university.province, university.typing,
                  university.score, university.education_level)
        # 执行sql语句
        self.cursor.execute(sql, values)
        # 提交数据
        self.conn.commit()

    # 查询数据
    def select_all(self):
        university_list = []
        sql = 'select * from university;'
        self.cursor.execute(sql)
        # 获取查询的结果集
        result_set = self.cursor.fetchall()
        # 遍历结果集
        for row in result_set:
            # row => (ranking, university_name, province, typing, score, education_level)
            ranking = row[0]
            university_name = row[1]
            province = row[2]
            typing = row[3]
            score = row[4]
            education_level = row[5]
            # 将数据封装为对象
            university = University(ranking, university_name, province, typing, score, education_level)
            # 将数据加到列表中
            university_list.append(university)
        # 返回列表对象
        return university_list

    # 关闭数据连接
    def close_db(self):
        self.conn.close()

# 创建一个 UniversitySpider 类
class UniversitySpider(object):
    # 初始化数据
    def __init__(self):
        # 创建一个数据库对象
        self.university_db = UniversityDB()
        # 定义访问的URL地址
        self.url = 'https://www.shanghairanking.cn/rankings/bcur/2023'

    # 执行爬取行为
    def crawl(self):
        try:
            response = urllib.request.urlopen(self.url)
            html = response.read().decode()
            soup = BeautifulSoup(html, 'html.parser')

            # 解析数据
            # 回顾: children 实现解析的时候, 会将回车, 空格 都作为子元素
            trs = soup.find('tbody').children  # trs是一个 list_iterator对象, 不能使用len()方法
            # 遍历trs
            for tr in trs:
                # print(type(tr), tr)     # <class 'bs4.element.NavigableString'>  <class 'bs4.element.Tag'>
                # children 获取的数据中有可能出现导航字符串, 就是回车和空格, 我们不需要
                # 判断 bs4.element.Tag
                if isinstance(tr, bs4.element.Tag):
                    # 取数据
                    # 获取每一个tr中的所有td标签
                    # tds = tr('td')
                    tds = tr.find_all('td')
                    # 排名
                    ranking = tds[0].text.strip()
                    # 大学名称
                    # university = tds[1].text.strip()
                    university_name = tds[1].find('a', attrs={'class': 'name-cn'}).text.strip()  # attrs
                    # 省份
                    province = tds[2].text.strip()
                    # 类型
                    typing = tds[3].text.strip()
                    # 总分
                    score = tds[4].text.strip()
                    # 办学层次
                    education_level = tds[5].text.strip()

                    # print(ranking, university_name, province, typing, score, education_level)

                    # 将获取的数据封装为一个数据模型对象
                    university = University(ranking, university_name, province, typing, score, education_level)
                    # 使用数据库对象插入数据的行为
                    self.university_db.insert_row(university)

        except BaseException as e:
            print(e)

    # 显示数据
    def show_data(self):
        # 让数据库对象查询所有数据, 并返回查询到的数据列表
        university_list = self.university_db.select_all()
        for university in university_list:
            print(university)

    # 关闭资源
    def close(self):
        self.university_db.close_db()


# 主函数
if __name__ == '__main__':
    # 1. 创建一个UniversitySpider对象
    spider = UniversitySpider()

    # 2. 执行爬取行为
    spider.crawl()

    # 3. 显示数据
    spider.show_data()

    # 4. 关闭资源
    spider.close()
