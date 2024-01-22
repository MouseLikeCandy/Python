# 进程  标准库multiprocessing
# 两种方法创建
# 方法一: 创建multiprocessing.Process实例
# 方法二: 创建一个类, 该类继承于multiprocessing.Process, 重写run方法

import os
import time
from multiprocessing import Process

# 实例实现
import pywin32_testutil


def worker(name):
    print(f'子进程名{name}, 子进程ID:{os.getpid()}')
    start = time.time()
    time.sleep(3)
    print(f'子进程{name}运行时间: {time.time() - start}')


if __name__ == '__main__':
    print(f'主线程ID:{os.getpid()}')
    print('start')
    # 创建子进程
    p1 = Process(target=worker, args=('process1',))
    p2 = Process(target=worker, args=('process2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('end')


# 继承实现
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self) -> None:
        print(f'子进程名: {self.name}, 子进程ID:{os.getpid()}')
        start = time.time()
        time.sleep(3)
        print(f'子进程{self.name}运行时间: {time.time() - start}')


if __name__ == '__main__':
    print(f'主进程ID: {os.getpid()}')
    print('start')
    # 创建子进程
    p1 = MyProcess('process1')
    p2 = MyProcess('process2')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('end')
