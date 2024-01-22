# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 20:01
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''添加操作'''
import mysql.connector

# 1.获取连接对象
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='123456', database='mydb3',
                               auth_plugin='mysql_native_password')
# 2.根据连接对象获取游标对象
cursor = conn.cursor()

# 3.准备sql语句, 并执行sql指令
sql = 'insert into exam(name, chinese, math, english) values(%s, %s, %s, %s);'
values = [
    ('李四', 64, 84, 94),
    ('王五', 65, 85, 95),
    ('赵六', 66, 86, 96)
]

cursor.executemany(sql, values)

# 4.提交数据
conn.commit()

print('执行完毕...')