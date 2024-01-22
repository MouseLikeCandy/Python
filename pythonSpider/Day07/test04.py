# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 20:29
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''删除操作'''
import mysql.connector


# 1.连接对象
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='123456', database='mydb3',
                               auth_plugin='mysql_native_password')

# 2.游标对象
cursor = conn.cursor()
# 3.执行sql对象
sql = 'delete from exam where name = %s;'   # 直接使用占位符, 不加引号
name1 = '张三'     # 字符串类型
name2 = ('张三')   # 字符串类型
name3 = ('李四',)  # 元组类型     只有一个元素必须加一个逗号才是元组类型   逗号表达式就是元组的自动拆分和合并
name4 = '李四',
print(type(name1), type(name2), type(name3), type(name4))  # test05
# def execute(self, operation, params=(), multi=False)   params为元组类型   类型不匹配
cursor.execute(sql, name3)
# 4.连接提交
conn.commit()

print('执行完成...')