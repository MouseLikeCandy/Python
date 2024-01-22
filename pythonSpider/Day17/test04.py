# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/8 12:15
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time

'''定义一个下载图片的任务'''
import threading
import urllib.request
import os

# 定义一个全局变量
isrunning = True
count = 1

# 定义一个下载图片的任务函数
def download_image():
    # count = 1     # count定义在内部, 在多个子线程时会有问题
    # 声明全局变量
    global count
    # 定义 url 地址
    url = f'http://127.0.0.1:5000/download?filename={count}.png'
    # 发送请求
    response = urllib.request.urlopen(url)
    # 获取response 对象中的data数据
    data = response.read()
    # 保存二进制数据到文件中
    if not os.path.exists('download'):
        os.mkdir('download')
    # 保存文件
    with open(f'download/{count}.png', mode='wb') as f:
        f.write(data)
        print(f'{count}.jpg 文件下载成功! ')
        count += 1

# 工作线程体函数, 是在子线程中执行的.
def workthread_body():
    # 循环工作
    while isrunning:
        print('工作线程体正在执行...')
        # 任务就是下载图片
        download_image()    # 调用下载图片的函数, 子线程中调用的函数, 同样也是在该子线程中执行的.
        # 模拟延时
        time.sleep(3)

    print('工作线程结束 ...')

# 控制线程体函数
def controlthread_body():
    global isrunning
    while isrunning:
        command = input()
        # 判断command指令, 然后执行不同的操作行为.
        if command == 'exit':
            isrunning = False
        else:
            print(f'command = {command}')
    print('控制线程结束 ... ')

if __name__ == '__main__':
    # 创建一个工作线程
    work_thread = threading.Thread(target=workthread_body)
    # 创建一个控制线程
    control_thread = threading.Thread(target=controlthread_body)

    # 启动线程
    work_thread.start()
    control_thread.start()