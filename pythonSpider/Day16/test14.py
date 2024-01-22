# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/3 18:33
@Auth ： 异世の阿银
@File ：test14.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import threading

'''
自定义函数实现线程体. threading.Thread(target=函数体名称) + 自定义函数
两部电影同时下载, 交替输出, 有时候换行没来得及输出
多线程的现象: 程序执行顺序是很难分析的.
'''

# 1. 定义一个'下载电影任务'的函数
def download_task(movie_name):
    # 获取当前线程的名称
    current_thread = threading.currentThread()
    while True:
        print(f'{current_thread.name} 下载 <{movie_name}> 电视剧')


if __name__ == '__main__':
    print('程序开始执行 ...')

    '''
    1. t1 = threading.Thread()创建对象的意思, 该方法会返回一个 Thread 线程对象.
    2. start() 启动线程. 该方法会在底层让操作系统为该进程开辟一条新的执行路径.
    # 思考: 开辟的新的执行路径, 执行什么代码???
    # 回答: 新开辟的执行路径执行的就是 target 指定的函数.
    
    说明: target 指定的是函数的名称, 不是调用该函数. 不加小括号.
        target 指定的函数, 只有在启动线程成功后, 程序底层自动帮助我们调用的.
    '''
    t1 = threading.Thread(target=download_task, name='下载线程1', args=('跨过鸭绿江', ))   # 元组
    t2 = threading.Thread(target=download_task, name='下载线程2', args=('我们结婚吧', ))
    t1.start()
    t2.start()

    print('程序继续向下执行 ...')


