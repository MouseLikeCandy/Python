# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/20 14:14
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
import threading
import time
import urllib.parse
import urllib.request

from pymongo import MongoClient
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
之前的翻页:
根据网址的规律
京东翻页:
点一下 "下一页" 实现
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class JDSpider():
    # 定义一个请求代理
    request_headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'}
    img_folder = 'JD_images'

    # 初始化数据
    def __init__(self):
        # selenium
        # 定义一个驱动对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()   # 窗口最大化

        # 将数据存储到 MongoDB 中
        try:
            # 创建客户端
            self.client = MongoClient('localhost', 27017)
            # 数据库
            self.db = self.client.jingdong
            # 集合
            self.collection = self.db.collection_jingdong
            # 标识
            self.opened = True
        except BaseException as e:
            print(e)
            self.opened = False
        # 创建存储图片的文件夹
        if not os.path.exists(JDSpider.img_folder):
            os.mkdir(JDSpider.img_folder)

    # 打开爬虫
    def open_spider(self, base_url, key):
        # 发送请求
        self.driver.get(base_url)
        # 获取搜索输入框对象
        key_input = self.driver.find_element(by=By.ID, value='key')
        key_input.send_keys(key)
        # key_input.click()   # 点击
        key_input.send_keys(Keys.ENTER)     # 回车键, 回车之后去哪个页面了?

    # 执行爬虫
    def process_spider(self):
        # 声明全局变量
        global no, threads
        # 进入页面之后, 滚动鼠标, 速度不能太快
        # 等待一会
        time.sleep(1)
        # 需求: 让页面滚动到底部 执行一段JS代码 window.scrollTo(0, document.body.scrollHeight);
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

        # 获取页面中指定的li标签
        lis = self.driver.find_elements(by=By.XPATH, value='//li[@class="gl-item"]')
        print(len(lis))

        for li in lis:
            # img 图片的 src
            try:
                src1 = li.find_element(by=By.XPATH, value='.//div[@class="p-img"]/a/img').get_attribute('src')
            except:
                src1 = ""

            try:
                src2 = li.find_element(by=By.XPATH, value='.//div[@class="p-img"]/a/img').get_attribute('data-lazy-img')
            except:
                src2 = ""

            # 价格
            try:
                price = li.find_element(by=By.XPATH, value='.//div[@class="p-price"]//i').text
            except:
                price = ''

            # detail详情, mark品牌
            try:
                detail = li.find_element(by=By.XPATH, value='.//div[@class="p-name p-name-type-2"]//em').text
                mark = detail.split(' ')[0]
            except:
                detail = ''
                mark = ''

            # 有时候src1有值, 有时候src2有值, src2不完整可以拼接
            # 图片名称
            if src1:    #1.jpg 2.jpg 3.jpg
                # 图片路径的资源拼接
                src1 = urllib.parse.urljoin(self.driver.current_url, src1)
                # img_file = str(no) + src1[src1.rfind('.')]  # 切出图片的后缀名jpg (如果后缀名不一致)
                img_file = str(no) + '.jpg'
            elif src2:
                src2 = urllib.parse.urljoin(self.driver.current_url, src2)
                img_file = str(no) + '.jpg'
            else:
                img_file = ''

            # 下载图片, 在子线程中实现
            if src1 or src2:
                # 多线程下载图片
                download_thread = threading.Thread(target=self.download, args=(src1, src2, img_file))
                download_thread.setDaemon(False)    # 后台线程, 默认就是False
                download_thread.start()
                # 将子线程添加到线程列表中
                threads.append(download_thread)

            # print(no, src1, src2, price, detail, mark)

            # 需要将 no, src1, src2, price, detail, mark 存储到MongoDB 的数据库中
            if self.opened:
                try:
                    # 封装数据字典
                    data_dict = {'no': no, 'price':price, 'detail': detail, 'mark': mark, 'img_file': img_file}
                    print(data_dict)
                    # 存储数据
                    self.collection.insert_one(data_dict)
                    # 编号自增
                    no += 1
                except BaseException as e:
                    print(e)

        # 完成了一页的数据, 接下来要找下一页, 翻页
        try:
            # selenium 做一个等待 等待下一页按钮出现
            locator = '//span[@class="p-num"]/a[@class="pn-next"]'
            WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))
            # 之前已经做了等待 sleep, 此处可以考虑不等待
            next_page = self.driver.find_element(by=By.XPATH, value='//span[@class="p-num"]/a[@class="pn-next"]')
            # 点击一下
            next_page.click()
            # 递归调用
            self.process_spider()   # 递归调用会因为异常结束
        except BaseException as e:
            print(e)


    # 关闭爬虫
    def close_spider(self):
        self.driver.close()

    # 下载图片任务
    def download(self, src1, src2, img_file):
        # data = b''    # 字节数据
        data = None
        # 发送请求
        if src1:
            try:
                # 将程序模拟成浏览器, 定义请求头 request_headers
                # 创建一个 request 对象
                request = urllib.request.Request(src1, headers=JDSpider.request_headers)
                # response = urllib.request.urlopen(src1)     # 直接使用就是 Python 程序发送请求, 而不是浏览器
                response = urllib.request.urlopen(request)
                data = response.read()  # 图片数据就是二进制数据
            except BaseException as e:
                print(e)
        if src2:
            try:
                # 将程序模拟成浏览器, 定义请求头 request_headers
                # 创建一个 request 对象
                request = urllib.request.Request(src1, headers=JDSpider.request_headers)
                # response = urllib.request.urlopen(src1)     # 直接使用就是 Python 程序发送请求, 而不是浏览器
                response = urllib.request.urlopen(request)
                data = response.read()  # 图片数据就是二进制数据
            except BaseException as e:
                print(e)

        # 判断
        if data:    # data有数据
            # 存储数据
            with open(JDSpider.img_folder + '/' + img_file, mode='wb') as f:
                f.write(data)
                print(f'download - {img_file}')







if __name__ == '__main__':
    # 定义一个全局使用的数据序号
    no = 1  # number

    # 定义线程列表
    threads = []

    # 1.创建一个京东爬虫对象
    spider = JDSpider()

    # 2.打开爬虫(关键字设置)
    spider.open_spider('https://www.jd.com/', '手机')

    # 3.执行爬虫(解析数据)
    spider.process_spider()

    # 4.存储数据

    # 5.关闭爬虫
    spider.close_spider()

    # 将子线程插入到主线程之前执行
    for thread in threads:
        thread.join()


    print('程序执行完成.')