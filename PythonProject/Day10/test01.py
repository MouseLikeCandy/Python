# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 21:50
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    综合案例: 学生管理系统
    功能:完成学生数据的增删改查(学号  姓名 年龄 成绩) 学号不重复
    先写主函数
    # 思考: 学生数据如何实现存储?使用什么数据类型实现学生数据的存储? 变量, 列表, 字典
    学生数据存储格式: 列表[字典{'1001':'name=张三, age=18, score=88'},{'1002':'name=李四, age=28, score=98'},...]
'''
# 查看所有学生
def query_students():
    print(f'查询学生')
    # 1.确保stus中有数据
    if len(stus) == 0:
        # 条件成立,列表为空
        print(f'亲, 目前没有任何学生数据')
        return
    print('-' * 100)
    # 2.遍历stus
    for stu_dict in stus:
        print(stu_dict)


def add_students():
    print(f'添加学生')
    while True:
        # 1.1 stu_id一定保证不能重复
        stu_id = input('亲, 请输入添加的学生学号, 如(1001):')
        # 1.2 遍历stus列表,取出列表中的所有key, 判断输入的stu_id是否在字典中已经存在的key重复了.
        for stu_dict in stus:
            if stu_id in stu_dict.keys():
                # 条件成立, 说明用户输入的stu_id已经被占用
                print(f'stu_id = {stu_id}已经存在了')    # 一旦学号重复,需要提示用户重新输入学号
                break   # 跳出for循环
        else:   # 表示for循环正常结束后执行到额代码, 没有遇见break
            print(f'stu_id = {stu_id}可以被使用')
            break  # 跳出while True循环
    # 2. name, age, score
    name = input('亲, 请输入学生的姓名:')
    age = input('亲, 请输入学生的年龄:')
    score = input('亲, 请输入学生的成绩:')

    # 3. 将用户输入的数据包装为字典类型的数据
    # 学生信息字典格式
    stu_dict = {stu_id: f'name={name}, age={age}, score={score}'}
    stus.append(stu_dict)
    print(f'添加成功')


def update_students():
    print(f'修改学生')
    # 根据学生的学号进行学生信息修改
    stu_id = input('亲, 请输入需要修改的学生学号: ')
    # 2. 判断stu_id是否在stus列表中存在
    # 定义一个学生下标的变量
    stu_index = -1
    for index, stu_dict in enumerate(stus):    # enumerate(列表)完成元素与下标的对应
        if stu_id in stu_dict.keys():
            # 条件成立,stu_id存在
            # 跳出之前找到stu_dict在stus对应的下标位置
            stu_index = index
            break   # 跳出for循环
    # 3. 判断stu_index下标值
    if stu_index == -1:
        # 学生学号没找到
        print(f'没有该学号的学生数据')
    else:
        # 学号存在
        stu_dict = stus[stu_index]
        print(stu_dict)

    # 4. 提示用户输入该学号对应学生的新的name, age, score
    name = input('亲, 请输入学生新的姓名:')
    age = input('亲, 请输入学生新的年龄:')
    score = input('亲, 请输入学生新的成绩:')

    # 包装新数据
    new_stu_dict = {stu_id: f'name={name}, age={age}, score={score}'}

    # 替代 stus 列表中原来对应的数据
    stus[stu_index] = new_stu_dict


def delete_students():
    print(f'删除学生')
    # 根据学生stu_id删除学生
    # 1.提示用户输入要删除的学生学号
    stu_id = input('亲, 请输入需要删除的学生学号: ')
    # 2. 判断stu_id是否在stus列表中存在
    # 定义一个学生下标的变量
    stu_index = -1  # 不要写0, -1 是不正常的下标
    for index, stu_dict in enumerate(stus):  # enumerate(列表)完成元素与下标的对应
        if stu_id in stu_dict.keys():
            # 条件成立,stu_id存在
            # 跳出之前找到stu_dict在stus对应的下标位置
            stu_index = index
            break  # 跳出for循环
    # 3. 判断stu_index下标值
    if stu_index != -1:
        # 学生学号找到了

        stu_dict = stus[stu_index]
        print(stu_dict)
        # 3.2 删除是一个很危险的操作, 最好与用户进行二次确认
        choice = input('亲, 确定删除该学生数据吗? (y删除/n取消):')
        if choice.lower() == 'y':
            # 删除
            stus.pop(stu_index)
            print('删除成功')
        else:

            print('取消删除操作')

    else:
        # 学号不存在
        print(f'没有该学号的学生数据, 无法删除')



if __name__ == '__main__':
    # 全局变量的数据(在主函数中定义的变量是全局变量,在自定义函数中可以被访问)
    # 定义了一些学生数据
    stus = [{'1001': 'name=张三, age=18, score=88'}, {'1002': 'name=李四, age=28, score=98'}, {'1003': 'name=王五, age=23, score=68'}]

    # 保证程序不结束
    while True:
        # 1. 界面展示
        menu = '''
        ----- 欢迎来到学生管理系统 V 1.0-----
            1.查看所有学生
            2.添加学生
            3.修改学生
            4.删除学生
            5.退出程序
        '''
        print(menu)
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
            break
        else:
            # 操作码不在指定范围内,提示错误
            print('亲, 操作码错误,请重新输入操作码')



