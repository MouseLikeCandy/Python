# 创建方法
"""
方法一: 创建threading.Thread实例, 将需要被线程执行的函数传入该实例.
方法二: 创建一个类, 该类继承于threading.Thread, 重写run方法
"""

import time
import threading

"""
# 方法一
def longtime(n):  # 需要被线程执行的函数
    time.sleep(n)


def main():
    # 实例化线程
    t = threading.Thread(target=longtime, args=[10])
    t.start()
    t.join()
    print('Done')


main()
"""

# 方法二
# import time
# import threading

"""
class MyThread(threading.Thread):
    def __init__(self, func, args, t_name=''):
        # 调用父类构造函数
        super().__init__()
        self.t_name = t_name
        self.func = func
        self.args = args

    # 线程执行的具体逻辑
    def run(self):
        self.func(self.args)


def longtime(n):
    time.sleep(n)


def main():
    # 实例化线程
    t = MyThread(longtime, 10, longtime.__name__)
    t.start()
    t.join()
    print('Done')


main()
"""


class MyThread(threading.Thread):
    def __init__(self, input, output):
        super().__init__()
        self.input = input
        self.output = output

    def run(self):
        for line in self.input.readlines():
            time.sleep(1)
            self.output.write(line)
        print("Thread Done")


def main():
    txt1 = open('1.txt', 'r')
    txt2 = open('2.txt', 'r')
    txt3 = open('3.txt', 'a')
    t1 = MyThread(txt1, txt3)
    t2 = MyThread(txt2, txt3)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


main()
