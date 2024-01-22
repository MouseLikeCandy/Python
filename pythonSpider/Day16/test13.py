# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/3 18:29
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import threading

if __name__ == '__main__':
    # 1. 查看当前线程
    c_thread = threading.currentThread()
    print(c_thread)     # <_MainThread(MainThread, started 25140)>  当前线程是主线程

    print(c_thread.name)
    print(c_thread.getName())

    # 2. 当前活动的有几个线程
    active_count = threading.active_count()
    print(active_count)

    # 3. 获取主线程对象
    m_thread = threading.main_thread()
    print(m_thread)


