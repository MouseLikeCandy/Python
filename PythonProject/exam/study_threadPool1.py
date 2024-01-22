# 线程池   concurrent标准库
import time
from concurrent.futures import ThreadPoolExecutor

# 创建具有5个线程的线程池
executor = ThreadPoolExecutor(5)


def longtime(s):
    time.sleep(s)
    print(f'sleep {s} second')


for i in range(10):
    # 将任务提交到线程池执行
    executor.submit(longtime, i)
    print(i)
