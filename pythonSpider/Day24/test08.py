# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/20 13:33
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium.webdriver.common.by import By

'''
实例: 爬取京东 手机
https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA

先考到自己的服务端进行测试 server4.py 他的图片是自动显示的
拿数据 检查-鼠标定位li-右键'以HTML格式修改'-CTRL+C V 
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 定义一个驱动对象
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://127.0.0.1:5000')

    # 解析数据
    li = driver.find_element(by=By.XPATH, value='//li[@class="gl-item"]')
    # img 图片的 src
    try:
        src1 = li.find_element(by=By.XPATH, value='.//div[@class="p-img"]/a/img').get_attribute('src')
    except:
        src1 = ""

    '''
    # source-data-lazy-img 源数据懒加载图片,是没有值的 src 是有值的
    # 后面的li中的img是没有 src 属性的, 而是在data-lazy-img里面
    页面的懒加载, 需要时再加载
    
    正真访问京东网站是可能是找不到src属性的.(前面有, 后面没有)  使用try catch处理
    '''
    try:
        src2 = li.find_element(by=By.XPATH, value='.//div[@class="p-img"]/a/img').get_attribute('data-lazy-img')
    except:
        src2 = ""

    # 价格
    try:
        price = li.find_element(by=By.XPATH, value='.//div[@class="p-price"]//i').text
    except:
        price = ''

    # 价格
    try:
        detail = li.find_element(by=By.XPATH, value='.//div[@class="p-name p-name-type-2"]//em').text
        mark = detail.split(' ')[0]
    except:
        detail = ''
        mark = ''



    print(src1, src2, price, detail, mark)
