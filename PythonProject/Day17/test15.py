# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 21:31
@Auth ： 异世の阿银
@File ：test15.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
shelve模块: 对象持久化模块
提供基本的存储操作, 构造一个简单的数据库, 像字典一样操作, 实现数据的存储和获取.
使Python程序间实现数据共享和持久化.(不通用)
键: 必须是字符串, 并且唯一
值: 任何类型的Python对象

注意点:
一开始必须打开shelve, 并且在修改之后一定要关闭shelve, Python语言独有, 不具有数据的共享性.
'''
from Day17.model import Student
import shelve

if __name__ == '__main__':
    # 1. 打开shelve
    stus = shelve.open('stus')
    # 2. 创建多个学生对象
    stu1 =Student('1001', '张三', 18, 66)
    stu2 = Student('1002', '张四', 16, 76)
    stu3 = Student('1003', '李四', 15, 96)
    stu4 = Student('1004', '王五', 14, 65)
    stu5 = Student('1005', '田七', 19, 63)


    # 存储数据  # 对应三个数据  stus.bak  stus.dat  stus.dir 不需要关心
    stus[stu1.stu_id] = stu1
    stus[stu2.stu_id] = stu2
    stus[stu3.stu_id] = stu3
    stus[stu4.stu_id] = stu4
    stus[stu5.stu_id] = stu5

    # 3. 关闭shelve
    stus.close()