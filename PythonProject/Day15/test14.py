# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 15:34
@Auth ： 异世の阿银
@File ：test14.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
文件读取
'''

# 1. 打开文件
file = open('file.txt', 'rt', encoding='utf-8')

# 光标seek
# 2.1 读取数据
content = file.read()
print(content)

# 将光标移动到开始处
file.seek(0)

# 2.2 按行读取
lines = file.readlines()
print(lines)

# 将光标移动到开始处
file.seek(0)

# 2.3 按行读取
for line in file.readlines():
    # 思考: 如何解决两个换行的问题?
    # 解决一: print(end=')
    # 解决二: '你好\n'  能不能将字符串中换行去掉呢??? 字符串对象.strip()  去掉头尾的空格与换行符
    # print(line, end='')
    line = line.strip()
    print(line)

# 3. 关闭文件
file.close()

