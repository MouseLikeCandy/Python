# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/13 17:54
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os.path
import random
import time
import urllib.request

from bs4 import BeautifulSoup
import threading

'''
爬取中国天气网的图片
http://www.weather.com.cn/

解决单线程的卡顿问题 —— 多线程
'''


# 定义一个下载图片的函数（耗时操作）
def download_image(src):
    # 模拟延时
    time.sleep(random.randint(1, 3))

    # 首先取出 src 中的图片名称
    image_name = os.path.basename(src)
    # 发送请求
    response = urllib.request.urlopen(src)
    # 直接取出二进制数据
    data = response.read()
    # 将数据保存到指定文件夹中
    with open('images/' + image_name, 'wb') as f:
        f.write(data)
        print(f'download - {image_name}')


# 定义一个图片爬取函数
def image_spider(url):
    # 声明全局变量(主函数定义的变量)
    global images_url, download_threads
    # 创建一个image文件夹
    if not os.path.exists('images'):
        os.mkdir('images')
    try:
        # 发送请求
        response = urllib.request.urlopen(url)
        # 获取数据
        html = response.read().decode()
        # print(html)     # 查看网页和浏览器中看到的是否一样
        # 将数据封装为文档树对象
        soup = BeautifulSoup(html, 'html.parser')
        # 获取所有的img标签
        imgs = soup.select('img')
        print(len(imgs))
        # 遍历imgs标签列表
        for img in imgs:
            # print(img)
            src = img['src']
            # print(src)  # 许多重复的, src是完整的路径, 可以直接发请求
            # 先判断,后添加
            if src not in images_url:
                # 将当前的src添加到图片列表中
                images_url.append(src)
                # 发送图片请求, 将下载图片任务放到子线程中执行, 用函数名称实现多线程
                download_thread = threading.Thread(target=download_image, name='图片下载线程', args=(src, ))
                # 启动下载线程
                download_thread.start()
                # 将子线程添加到下载线程列表中
                download_threads.append(download_thread)

    except BaseException as e:
        print(e)


if __name__ == '__main__':
    # 定义一个图片请求的列表
    images_url = []
    # 定义一个子线程列表     # 主程序最开始就会结束输出 completed！
    download_threads = []
    # 定义一个url地址
    url = 'http://www.weather.com.cn/weather1d/101010100.shtml'
    # 图片爬取
    image_spider(url)

    # 遍历子线程列表，让每一条子线程都插入到主线程之前执行
    for download_thread in download_threads:
        download_thread.join()
    print('completed!')     # 最后输出completed!
