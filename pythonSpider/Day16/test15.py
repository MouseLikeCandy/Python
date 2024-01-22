# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/3 18:57
@Auth ： 异世の阿银
@File ：test15.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import threading
'''
自定义线程类实现线程体. class TestThread(threading.Thread) + 重写 run() 方法
'''

# 自定义类实现下载任务线程类
class DownloadThread(threading.Thread):
    # 初始化
    def __init__(self, thread_name, movie_name):
        # 父类中有线程名称的参数 thread_name
        # super(DownloadThread, self).__init__(name=movie_name)
        super().__init__(name=thread_name)  # 父类的数据传给父类初始化
        self.movie_name = movie_name        # 子类的数据子类初始化

    # 必须重写父类 Thread 的run()方法
    # run()方法是在线程启动后需要执行的代码(子线程执行的代码)
    def run(self) -> None:
        # 父类run()方法除了调用 target 指定的函数外, 没有其他功能.
        # 获取当前线程的名称
        current_thread = threading.currentThread()
        while True:
            print(f'{current_thread.name} 下载 <{self.movie_name}> 电视剧')


if __name__ == '__main__':
    print('程序开始执行 ...')

    # 创建 DownloadThread 对象
    t1 = DownloadThread('下载线程1', '跨过鸭绿江')  # 元组
    t2 = DownloadThread('下载线程2', '我们结婚吧')
    t1.start()
    t2.start()

    print('程序继续向下执行 ...')