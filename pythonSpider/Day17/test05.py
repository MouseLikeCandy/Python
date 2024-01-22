# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/8 12:47
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import random
import threading
import time

'''多条线程抢同一资源的处理'''
'''
模拟银行取现的操作
柜台取钱 + 提款机取钱 一起取
'''
# 定义一个取现类
class FetchMoney(threading.Thread):
    # 初始化方法
    def __init__(self, bank, thread_name):
        super().__init__(name=thread_name)
        self.bank = bank

    # 重写run()方法
    def run(self)->None:
        number = self.bank.getMoney(400)
        print(f'{threading.currentThread().name} 获取取款金额: {number}')

# 创建一个银行类
class Bank(object):
    # 初始化方法
    def __init__(self, money):
        self.money = money

    # 取现
    def getMoney(self, number):
        print(f'{threading.currentThread().name} 执行取款操作...')
        # 逻辑处理
        if number < 0:
            return -1   # 表示取款金额为负数
        elif number > self.money:
            return -2   # 表示取款金额大于存款余额
        elif self.money < 0:
            return -3   # 账号没有余额
        else:
            # 模拟 CPU切换  # CPU很可能在这里发生切换, 一旦出现程序便出错 (模拟网络延迟) 多线程造成的安全问题
            time.sleep(random.randint(1, 3))
            # CPU 如果在此处切换, 程序就是错的. 多线程抢夺共享资源就可能会造成资源错误.
            # 模拟正常取现
            self.money -= number    # 减少存款余额
            print(f'{threading.currentThread().name} 剩余金额: {self.money}')
            return number


if __name__ == '__main__':
    # 1. 创建一个银行类
    bank = Bank(600)    # 存600块

    # 2. 模拟两条线程同时执行取现行为
    # 2.1. 创建一个柜台线程(类/函数)
    t1 = FetchMoney(bank, '柜台线程')
    # 2.2. 创建一个ATM线程(类/函数)
    t2 = FetchMoney(bank, 'ATM线程')

    # 3. 启动线程
    t1.start()
    t2.start()
