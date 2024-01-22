# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/14 15:10
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
文件操作
上下文管理器: context Manager
自动上线了 __enter__()和__exit()方法
with 语句 
with as    关闭文件时,推荐使用

Python语言提供了一个上下文管理器对象open()
'''

# 自定义一个上下文管理器
class MyContextManager(object):
    # 入口方法
    def __enter__(self):
        print('__enter__方法被调用了.')
        return self

    # 操作方法
    def operate_file(self):
        print('正在操作文件中...')

    # 出口方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了.')



if __name__ == '__main__':
    # 上下文管理器与with共同使用
    # with 上下文管理器对象 as
    # with语句和上下文管理器对象共同使用, 内部会自动执行enter & exit方法
    with MyContextManager() as f:
        f.operate_file()
        f.operate_file()
