# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/8 12:04
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''停止线程'''
import threading
import time

# 定义一个全局变量
isrunning = True

# 工作线程体函数
def workingthread_body():
    # 执行一段代码, 然后停止, 指定时间后继续循环该操作.
    while isrunning:
        print('工作线程正在执行中...')
        time.sleep(3)

    print('工作线程结束...')

# 工作线程体函数
def controlthread_body():
    global isrunning    # 声明全局变量
    while isrunning:
        # 等待用户的一条指令
        command = input()     # 这样写表示没有提示信息, 但是一直等待输入
        if command == 'exit':
            isrunning = False
        elif command == 'enter':
            pass
        elif command == 'running':
            pass
        else:
            print(f'command = {command}')


if __name__ == '__main__':
    # 创建一个工作线程对象
    work_thread = threading.Thread(target=workingthread_body)
    # 启动工作线程
    work_thread.start()
    # 创建一个控制线程
    control_thread = threading.Thread(target=controlthread_body)
    # 启动控制线程
    control_thread.start()

