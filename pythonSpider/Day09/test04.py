# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/9 18:04
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''

'''
import mysql.connector
# 1. 获取连接对象
# 说明 : MySQL 8.0 版本后, 需要设置 auth_plugin='mysql_native_password' 参数
conn = mysql.connector.connect(host='localhost', user='root', password='123456',
database='student_db', auth_plugin='mysql_native_password')
# 2. 获取 cursor 对象
cursor = conn.cursor()
# 3. 编写 sql 语句

sql = 'insert into students(stu_id, name, age, score) values(%s, %s, %s, %s);'
values = [
('1001', '张三', 18, 88.0),
('1002', '李四', 20, 55.0),
('1003', '王五', 30, 66.0),
('1004', '赵六', 18, 11.0),
('1005', '田七', 20, 33.0),
('1006', '麻八', 30, 22.0),
('1007', '小二', 18, 44.0),
('1008', '老一', 20, 99.0),
('1009', '赵九', 30, 77.0)
]
# 4. 执行 sql 语句
cursor.executemany(sql, values)
# 5. 提交
conn.commit()
print('插入数据成功!')