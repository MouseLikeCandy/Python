# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/12 19:32
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import urllib.request
from bs4 import BeautifulSoup
import mysql.connector
'''
爬取'天气网'

# 爬取数据, 封装为某一类型, 存储到数据库中, 后续操作从数据库中实现
# 从数据库中获取该类的列表 
'''

# 定义一个'Weather'类
class Weather(object):
    # 属性
    def __init__(self, city, date, wea, temperature, wind):
        self.city = city
        self.date = date
        self.wea = wea
        self.temperature = temperature
        self.wind = wind

    def __str__(self):
        return f'Weather[city = {self.city}, date = {self.date}, wea = {self.wea}, ' \
               f'temperature = {self.temperature}, wind = {self.wind}]'


# 定义一个 'WeatherDB' 类
class WeatherDB(object):
    # 初始化数据, 需要初始化数据库与数据表
    def __init__(self):
        # 数据库
        sql_db = 'CREATE DATABASE IF NOT EXISTS weather_db ;'
        # 获取连接对象
        self.conn = mysql.connector.connect(host='localhost', user='root', password='123456', auth_plugin='mysql_native_password')
        # 获取游标对象
        self.cursor = self.conn.cursor()
        # 执行创建数据库的行为
        self.cursor.execute(sql_db)
        # 切换数据库
        self.cursor.execute('use weather_db;')
        # 创建数据表     # 联合主键
        sql_table = '''
            create table weather(
            city varchar(8),
            date varchar(16),
            wea varchar(16),
            temperature varchar(16),
            wind varchar(16),
            primary key(city, date)
            );
        '''
        try:
            # 创建表格
            self.cursor.execute(sql_table)  # 第一次执行程序, 表格不存在不会报错
        except BaseException as e:
            # 一旦程序来到这里, 说明表格已经存在
            print(e)
            print('数据表已经存在了. 需要删除表格中的数据 ...')
            self.cursor.execute('delete from weather;')

    # 插入数据的行为
    def insert_row(self, weather):
        # 写一个插入数据的sql
        sql = 'insert into weather(city, date, wea, temperature, wind) values(%s, %s, %s, %s, %s);'
        values = (weather.city, weather.date, weather.wea, weather.temperature, weather.wind)
        # 执行插入行为
        self.cursor.execute(sql, values)
        # 提交数据
        self.conn.commit()

    # 查询全部数据的行为
    def query_all(self):
        # 定义一个weather_list列表
        weather_list = []
        # sql语句
        sql = 'select * from weather;'
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取结果集
        result_set = self.cursor.fetchall()
        # 遍历结果集
        for row in result_set:
            # row => (city, date, weather, temperature, wind)
            city = row[0]
            date = row[1]
            wea = row[2]
            temperature = row[3]
            wind = row[4]
            # 将取出的数据封装为Weather对象
            weather = Weather(city, date, wea, temperature, wind)
            # 将weather对象存储到列表中
            weather_list.append(weather)
        # 将天气列表返回
        return weather_list

    # 关闭资源
    def close_db(self):
        # 关闭连接对象
        self.conn.close()


# 定义一个'WeatherForcast'类
class WeatherForcast(object):
    # 初始化数据
    def __init__(self):
        # 初始化一个 self.weather_db 对象
        self.weather_db = WeatherDB()
        # 初始化城市代码
        self.city_code = {
            '北京': '101010100',
            '上海': '101020100',
            '广州': '101280101',
            '深圳': '101280601'
        }

    # 根据城市, 查询对应城市的数据
    def forcast_city(self, city):
        # 1. 判断
        if city not in self.city_code.keys():
            # 条件成立, 说明city这个key不存在
            print(f'{city} code can not be found.')
            return  # 提前结束该行为
        # 2. 根据city取出对应的城市的代码
        city_code = self.city_code[city]  # 如果city这个key不存在.程序会报keyError错误
        # 3. 拼接请求的url
        url = f'http://www.weather.com.cn/weather/{city_code}.shtml'
        # 4. 发送请求
        # 异常处理
        try:
            # 1. 确认请求的url地址
            # 2. 发送请求
            response = urllib.request.urlopen(url)
            # 3. 获取响应中的数据
            html = response.read().decode()
            # 4. 将html字符串类型的数据转换为'文档树'结构
            soup = BeautifulSoup(html, 'html.parser')
            # 5. 使用soup对象实现页面解析
            lis = soup.select('ul[class="t clearfix"] > li')  # select()方法返回的是一个列表
            # 6. 遍历列表
            for li in lis:  # li的类型也是bs4.element.tag 标签类型, 因此依然可以调用 'find, find_all, select' 方法查找数据
                # 去浏览器分析
                # 6.1 日期
                date = li.select('h1')[0].text  # select()方法返回的数据哪怕只有一条数据也是列表类型, 因此取数据时使用下标.
                # 6.2 天气
                weather = li.select('p[class="wea"]')[0].text
                # 6.3 温度
                temperature = li.select('p[class="tem"]')[0].get_text().strip()  # 只取外层的p标签, 去除数据首尾空格和换行
                # 6.4 风力
                wind = li.select('p[class="win"] > i')[0].text

                # 将获取的数据封装为一个Weather对象
                # print(city, date, weather, temperature, wind)
                weather = Weather(city, date, weather, temperature, wind)
                # 将封装完毕的 weather 对象传递给数据库对象, 执行数据的插入
                self.weather_db.insert_row(weather)

        except BaseException as e:
            print(e)

    # 展示数据
    def show_data(self):
        # 直接调用数据库对象的查询方法, 然后接收返回的列表数据
        weather_list = self.weather_db.query_all()
        # 遍历 weather_list 列表
        for weather in weather_list:
            print(weather)      # 如果没有重写 weather对象的 str 方法, 输出的结果就是对象的地址

    # 关闭资源
    def close(self):
        self.weather_db.close_db()


# 主函数
if __name__ == '__main__':
    # 需求: 爬取天气预报数据, 存储到数据库中
    # 1. 创建一个天气预报对象
    wf = WeatherForcast()

    # 2. 定义一个城市列表
    cities = ['北京', '上海', '广州', '深圳', '西藏']

    # 3. 遍历城市列表
    for city in cities:
        # 使用天气预报对象实现指定城市的数据获取
        wf.forcast_city(city)

    # 4. 展示数据
    wf.show_data()

    # 5. 关闭资源
    wf.close()

    print('completed ! ')
