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
'''


# 创建一个TicketWindow类
class TicketWindow(threading.Thread):
    # 类数据
    tickets = 1000   # 类数据被该类的所有对象所共享, 并且在内存中仅有一份.
    # 定义一把锁变量
    lock = threading.RLock()

    # 初始化方法
    def __init__(self, thread_name):
        super().__init__(name=thread_name)

    # 重写run()
    def run(self) -> None:
        # 循环卖票, 直到将所有的票全部卖完
        while True:
            try:
                # 获取锁, 锁住if整体
                TicketWindow.lock.acquire()
                if TicketWindow.tickets > 0:
                    # 模拟CPU在此处切换
                    # time.sleep(random.randint(1, 3))
                    # 有票
                    print(f'{threading.currentThread().name} 正在售出第{TicketWindow.tickets} 张票.')
                    # 票数递减
                    TicketWindow.tickets -= 1
                else:
                    # 没票, 结束循环, 循环一结束线程也就结束了
                    # 加锁之后程序没有结束的问题: 跳出之前并没有将锁释放
                    break
            # 释放锁
            finally:
                TicketWindow.lock.release()     # 释放锁在finally最安全


if __name__ == '__main__':
    # 创建三个售票窗口
    t1 = TicketWindow('窗口1')
    t2 = TicketWindow('窗口2')
    t3 = TicketWindow('窗口3')

    # 启动线程
    t1.start()
    t2.start()
    t3.start()

