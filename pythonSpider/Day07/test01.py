# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 19:30
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
MySQL 驱动  连接库
安装 mysql-connector
安装第三方库  pip install mysql-connector
测试: import mysql.connector
常用操作:
插入数据:insert
查询数据:select
更新数据:update
删除数据:delete
'''
# 准备数据mydb3
# 打开MySQL服务


# 创建数据库连接
'''
# 数据操作步骤
# 1.获取连接对象
# 2.获取cursor对象
# 3.编写sql语句
# 4.执行sql语句
# 5.提交
# 6.关闭资源
'''
import mysql.connector

# 1.获取mysql服务的连接对象
conn = mysql.connector.connect(host='localhost', user='root', password='123456', database='mydb3',
                               auth_plugin='mysql_native_password')     # 8.0之后需要添加, mysql本地密码

# 2.获取连接对象的'游标'对象
cursor = conn.cursor()
# 3.通过'游标'对象执行sql指令
# sql语句中需要使用%s作为参数的占位符
sql = 'insert into exam(name, chinese, math, english) values(%s, %s, %s, %s);'
values = ('张三', 66, 88, 99)
cursor.execute(sql, values)     # 位置传参
# cursor.execute(operation=sql, params=values)   # 关键字传参



# 连接对象拥有提交数据到数据库服务的功能
# 说明: 之前命令行和图形化界面中没有进行提交操作, 是因为命令行和图形化界面都会实现自动提交, 程序中我们需要手动提交
conn.commit()


print(conn) # <mysql.connector.connection.MySQLConnection object at 0x000001ECD82EEEF0> 内存地址
print('执行完毕...')


