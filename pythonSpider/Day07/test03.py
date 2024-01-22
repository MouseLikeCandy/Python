# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 20:15
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 查询: 因为不涉及到数据的修改,所以无需提交操作
'''查询操作'''
import mysql.connector

# 1.连接对象
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='123456', database='mydb3',
                               auth_plugin='mysql_native_password')
# 2.游标对象
cursor = conn.cursor()
# 3.执行sql语句
sql = 'select * from exam;'
cursor.execute(sql)
# result = cursor.execute(sql)    # 说明execute()方法是没有返回结果的
# print(result)   # None

# 4.获取查询结果
result_set = cursor.fetchall()  # fetch 拿来,提取   result_set 列表 + 元组元素的类型
# result_set = cursor.fetchone()  # fetchone() 登录时使用, 账号密码正确返回一个结果, 错误没有结果
# result_set = cursor.fetchmany(3)  # fetchmany(size) 分页
# 遍历列表
for result in result_set:
    print(result)


