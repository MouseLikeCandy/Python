# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：MySQL_database.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/8 14:57 
"""
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)   # db = 'spiders' 不区分大小写
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)


database_name = "Spiders"
# 使用SHOW DATABASES语句检查数据库是否存在
cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
# 获取检查结果
result = cursor.fetchone()
if not result:
    cursor.execute("CREATE DATABASE Spiders DEFAULT CHARACTER SET utf8mb4")

# 使用USE语句切换到指定的数据库
cursor.execute(f"USE {database_name}")

sql = 'CREATE TABLE IF NOT EXISTS students(' \
      'id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
cursor.execute(sql)

# 插入学生信息
id = '20140001'
user = '王小鱼'
age = 20

sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()

# 动态插入数据
data = {
    'id': '20140107',
    'name': '王小鱼',
    'age': 20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()

# 更新数据
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (28, '王小鱼'))
    db.commit()
except:
    db.rollback()

# 灵活插入、去重
data = {
    'id': '20140108',
    'name': '尹宁',
    'age': 42
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE '\
    .format(table=table, keys=keys, values=values)
print(sql)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()

# 删除数据
table = "students"
condition = 'age < 10'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
print(sql)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 查询
sql = 'SELECT * FROM students WHERE age > 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
db.close()
