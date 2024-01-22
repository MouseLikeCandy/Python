# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/9 1:49
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import random
import threading
import time

'''
需求: 售票系统, 三个窗口卖100张票

错误原因: 多线程 + CPU自由切换 , 修改了多条线程访问的共有变量.

定义为类数据的锁和定义为对象数据的锁的区别

类数据: 存储在代码区的类模板中,所有对象共享类中的同一份数据.
对象数据: 存储在堆区中的, 每一个对象都有独立的一份数据.

多线程的锁对象一定要保证唯一性.
'''


# 创建一个TicketWindow类
class TicketWindow(threading.Thread):
    # 类数据
    tickets = 10   # 类数据被该类的所有对象所共享, 并且在内存中仅有一份.
    # 定义一把锁
    # lock = threading.RLock()  # 类变量

    # 初始化方法
    def __init__(self, thread_name):
        super().__init__(name=thread_name)
        # 锁对象
        self.lock = threading.RLock()   # 对象变量

    # 重写run()
    def run(self) -> None:
        # 循环卖票, 直到将所有的票全部卖完
        while True:
            try:
                # 获取锁
                self.lock.acquire()
                if TicketWindow.tickets > 0:
                    # 模拟CPU在此处切换
                    # time.sleep(random.randint(1, 3))
                    # 有票
                    print(f'{threading.currentThread().name} 正在售出第{TicketWindow.tickets} 张票.')
                    # 票数递减
                    TicketWindow.tickets -= 1
                else:
                    # 没票, 结束循环, 循环一结束线程也就结束了
                    break
            finally:
                # 释放锁
                self.lock.release()


if __name__ == '__main__':
    # 创建三个售票窗口
    t1 = TicketWindow('窗口1')
    t2 = TicketWindow('窗口1')
    t3 = TicketWindow('窗口3')

    # 启动线程
    t1.start()
    t2.start()
    t3.start()
