# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 20:08
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
dir()作用: 查看对象内的所有属性和方法.包括所有内置与用户自定义的.
dir() -> directory 列出目录
'''


if __name__ == '__main__':
    str = 'hello world'
    # 需求: 查看字符串类型都有哪些数据和行为
    # 数据, 行为: 双下划线开头,说明这是私有数据和行为, 外部使用者是不能直接调用的.
    print(dir(str))

    num_list = [10, 20, 30]
    print(dir(num_list))

    name_dict = {'name': '张三'}
    print(dir(name_dict))



