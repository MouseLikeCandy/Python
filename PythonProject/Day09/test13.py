# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 21:50
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import sys

'''
    综合案例: 学生管理系统
    功能:完成学生数据的增删改查(学号  姓名 年龄 成绩) 学号不重复
    先写主函数
    # 思考: 学生数据如何实现存储?使用什么数据类型实现学生数据的存储? 变量, 列表, 字典
    # 学生数据: (id, name, age, score) -> {key: value}
    # 思考: key和value是什么类型的数据? 字符串
    # 学生数据: {'1001': 'name=张三, age=18, score=99'}
'''
# 查看所有学生
def query_students():
    print(f'查询所有学生')

def add_students():
    print(f'添加学生')

def update_students():
    print(f'修改学生')

def delete_students():
    print(f'删除学生')

if __name__ == '__main__':
    # 保证程序不结束
    while True:
        # 1. 界面展示
        menu = '''
        ----- 欢迎来到学生管理系统 -----
            1.查看所有学生
            2.添加学生
            3.修改学生
            4.删除学生
            5.退出程序
        '''
        # 2. 提示用户输入操作码
        choice = input('亲, 请输入执行的操作码: ')
        # 3. 用户操作码的判断
        if choice == '1':
            # 查看所有学生
            query_students()
        elif choice == '2':
            # 添加学生
            add_students()
        elif choice == '3':
            # 修改学生
            update_students()
        elif choice == '4':
            # 删除学生
            delete_students()
        elif choice == '5':
            # 退出程序
            print('感谢您的使用,下次再会!')
            sys.exit()  # 正常退出
            break
        else:
            # 操作码不在指定范围内,提示错误
            print('亲, 操作码错误,请重新输入操作码')



