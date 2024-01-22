# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 21:52
@Auth ： 异世の阿银
@File ：test15.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
多分支结构
需求：对一个学生的成绩进行等级划分
>=80 优秀
>=70 良好
>=60 中等
<60  差
'''
# 1.定义变量，接收用户输入：
score = int(input('亲，请输入您的成绩：'))

# 2.多分支结构     不管多少分支，最终仅执行一个。
if score >= 80:
    print(f'{score} 成绩等级为优秀')
elif score >= 70:
    print(f'{score} 成绩等级为良好')
elif score >= 60:
    print(f'{score} 成绩等级为中等')
else:
    print(f'{score} 成绩等级为差')

print('程序继续向后执行...')


# 一旦执行完毕某条分支，就会立即跳出这个整体

