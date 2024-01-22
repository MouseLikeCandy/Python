# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/13 17:54
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os.path
import urllib.request
from bs4 import BeautifulSoup

'''
爬取中国天气网的图片
http://www.weather.com.cn/

单线程下载
'''


# 定义一个下载图片的函数（耗时操作）
def download_image(src):
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
    global images_url
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
                # 发送图片请求 # 后期放到子线程中
                download_image(src)

    except BaseException as e:
        print(e)


if __name__ == '__main__':
    # 定义一个图片请求的列表
    images_url = []
    # 定义一个url地址
    url = 'http://www.weather.com.cn/weather1d/101010100.shtml'
    # 图片爬取
    image_spider(url)

    print('completed!')
