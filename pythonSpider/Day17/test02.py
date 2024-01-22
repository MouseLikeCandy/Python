# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/8 11:37
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
实现线程体主要有以下两种方式：
自定义函数实现线程体. threading.Thread(target=函数体名称) + 自定义函数
自定义线程类实现线程体. class TestThread(threading.Thread) + 重写 run() 方法
'''

'''

需求: 主线程结束, 所有的子线程都应该结束.
1. 前台线程: 主线程的执行完毕应该是在所有子线程都执行完毕后, 主线程最后才结束.
主线程如果结束, 前台线程就立即结束了.

2. 在主线程执行完毕前, 让所有的子线程插队到主线程前执行

后台线程:
如果一个程序有多条线程, 主线程结束并不意味着程序结束, 
如果主线程结束了, 子线程会继续执行, 直到执行完毕, 程序才会结束.
这个子程序就被称为'后台线程'.

插入join
'''
import threading
import time, random

# 定义一个函数, 这个函数是在子线程中被执行的.
def reading(n):
    for i in range(n):
        print(f'threading ... {i}')
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    # 创建一个线程对象
    t = threading.Thread(target=reading, args=(3,))    # 子线程默认有名称  -  thread -n

    # 前后台线程状态一定是在'线程启动前'实现设置
    t.setDaemon(False)  # 默认值, 默认当前线程为后台线程, 后台线程不会跟随主线程结束而结束.

    # 启动线程
    t.start()   # 启动了一条子线程

    t.join()    # 说明: 此处当前线程就是'主线程', t.join()这句代码就是让子线程插入到主线程之前执行.

    # 等待t线程执行完毕, 才能继续向下执行.
    '''我们未来可能将所有的子线程添加到列表中, 然后遍历子线程列表, 让每一个子线程都插队到主线程之前被执行.'''
    print(f'{threading.currentThread().name} end.')