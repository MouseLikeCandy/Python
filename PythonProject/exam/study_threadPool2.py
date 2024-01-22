import time
from concurrent.futures import ThreadPoolExecutor, as_completed

executor = ThreadPoolExecutor(5)


def longtime(s):
    time.sleep(s)
    return f'执行结果: {s + 10}'


all_task = []

for i in range(10):
    # 提交任务
    e = executor.submit(longtime, i)  # submit方法会返回future类型
    # 添加到list
    all_task.append(e)
    print(i)

#    print(e.result())   # 加入该输出之后输出结果不按顺序是何原因?
# 线程池的方法有返回值, 通过as_completed方法获取
for future in as_completed(all_task):
    # 获取线程池中任务执行的结果
    result = future.result()
    print(result)


