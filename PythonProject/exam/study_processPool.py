# 进程池
from multiprocessing import Pool, cpu_count
import os
import time
# from concurrent.futures import ProcessPoolExecutor

def worker(name):
    print(f'子进程名:{name}, 子进程ID: {os.getpid()}')
    time.sleep(1)

if __name__ == '__main__':
    print(f'主线程ID: {os.getpid()}')
    print('start')
    cpu_num = cpu_count()
    print(f'当前计算机CPU核心数: {cpu_num}')
    p = Pool(cpu_num)
    for i in range(10):
        p.apply_async(worker, args=(f'process{i}',))
    p.close()
    p.join()
    print('end')
