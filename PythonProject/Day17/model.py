# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 21:38
@Auth ： 异世の阿银
@File ：model.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# model 模型
'''

class Student:
    def __init__(self, stu_id=None, name=None, age=None, score=None):
        self.stu_id = stu_id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'Student [stu_id = {self.stu_id}, name = {self.name}, age = {self.age}, gender = {self.score}]'