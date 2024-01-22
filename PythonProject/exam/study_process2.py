# Queue队列在不同进程中传递信息
# 理解: 一个中间商
import time
import os
from multiprocessing import Process, Queue


# 生产者
def producer(q):
    print(f'producer PID: {os.getpid()}')
    with open('2.txt', 'r') as f:
        print(type(f))
        # 逐行读取
        for i in f.readlines():
            # 将i添加到对列
            q.put(i)
            time.sleep(1)


# 消费者
def consumer(q):
    print(f'consumer PID: {os.getpid()}')
    while True:
        # 获取队列中的内容
        i = q.get()
        print(f'获取生产者进程产生的内容: {i}')


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    c = Process(target=consumer, args=(q,))
    # 产生数据
    p.start()
    # 消费数据
    c.start()
    # 主进程挂起, 等待子进程
    p.join()
    # 子进程consumer是死循环, 无法等待其运行结束, 只可强行终止其运行
    c.terminate()
