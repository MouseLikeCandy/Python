# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 20:45
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''修改操作'''
import mysql.connector

# 1.连接对象
conn = mysql.connector.connect(host='localhost', user='root', password='123456', database='mydb3',
                               auth_plugin='mysql_native_password')
# 2.游标对象
cursor = conn.cursor()
# 3.sql
sql = 'update exam set chinese = %s, math = %s, english = %s where name = %s;'
values = (98, 99, 100, '关羽')
cursor.execute(sql, values)
# 4.提交
conn.commit()

print('执行完成...')