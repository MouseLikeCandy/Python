# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/3 18:21
@Auth ： 异世の阿银
@File ：test12.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


class Test(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        for i in range(3):
            print(f'{self.name} -> run ...{i}')


if __name__ == '__main__':
    print("main 线程开始执行....")

    # 创建一个Test对象
    test1 = Test('One')
    test1.run()

    # 再创建一个Test对象
    test2 = Test('Two')
    test2.run()

    print("main 线程结束执行....")