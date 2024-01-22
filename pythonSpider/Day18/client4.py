# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/12 20:26
@Auth ： 异世の阿银
@File ：client.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
多线程实现下载
主程序发请求, 图片下载没有阻塞请求的发送
主程序应该最后结束, 让子线程插队

每一张图片的 full_img_src 都是不一样的, 3张图片就有3个线程
'''
# 自定义一个函数, 一会需要递归调用
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import os
import time, random
import threading

# 定义一个下载图片的函数, 下载任务函数
def download_image(src):
    print(f'当前线程: {threading.currentThread().name} {threading.currentThread()}')

    # 1. 发送请求
    response = urllib.request.urlopen(src)  # 首先要给图片的 src 地址发送请求才能获取图片的二进制数据
    # 2. 获取图片的二进制数据
    data = response.read()
    # 3. 保存data二进制数据
    img_name = os.path.basename(src)
    if not os.path.exists('download'):
        os.mkdir('download')
    # 模拟耗时
    time.sleep(random.randint(3, 5))
    # 4. 保存数据
    with open('download/' + img_name, 'wb') as f:
        f.write(data)
    print(f'download {img_name}, len = {len(data)}')


def spider(url):
    # 声明 urls 全局列表
    global urls, threads

    # 每次发送之前都判断一下这个请求又没有发送过
    if url not in urls:
        # 每一个请求发送之前, 都先记录一下该请求的 url 地址
        urls.append(url)

        # 发送请求
        response = urllib.request.urlopen(url)
        # 获取数据
        html = response.read().decode()
        # print(html)
        # 将数据转换为文档树类型
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.find('h3').text
        print(text)
        # 获取div内容
        divs = soup.select('div')  # 可能存在多个div标签
        imgs = soup.select('img')
        # print(imgs)
        # print(f'len(divs) = {len(divs)}, len(imgs) = {len(imgs)}')
        if len(divs) > 0 and len(imgs) > 0:
            # 获取页面内容
            content = divs[0].text
            print(content)
            # 获取图片的src路径
            img_src = imgs[0]['src']    # 这是一个不完整的 img_src, 所以需要拼接
            full_img_src = urllib.parse.urljoin(url, img_src)
            print(full_img_src)

            # 下载图片, 可能是一个非常耗时的操作, 如果下载资源卡住了, 程序会发生什么情况?
            # download_image(full_img_src)    # 应该将下载图片的耗时操作放到子线程中执行
            download_thread = threading.Thread(target=download_image, name='图片下载线程', args=(full_img_src, ))
            download_thread.start()     # 子线程一起动, 就会自动调用target指定的线程名称.



            # 将子线程添加到 threads列表中
            threads.append(download_thread)


        # 获取页面中所有 a 超链接标签的 href 数值
        links = soup.select('a')
        for link in links:
            # 取出 link 中对应的 href 属性值
            href = link['href']
            # print(href)     # href 并不是一个完整的url

            # urllib.parse 请求的解析模块中有一个urljoin()方法可以只能完成url地址的拼接
            full_url = urllib.parse.urljoin(url, href)
            # print(full_url)

            # 再次发送请求
            spider(full_url)    # 直接使用递归调用


if __name__ == '__main__':
    # 定义一个url列表
    urls = []
    # 定义一个threads线程列表
    threads = []
    # 根路由
    url = 'http://127.0.0.1:5000/'
    # 调用爬虫函数
    spider(url)


    # 遍历threads列表, 让所有的子线程插队到主线程之前执行
    for download_thread in threads:
        download_thread.join()

    print('主线程执行完毕...')
