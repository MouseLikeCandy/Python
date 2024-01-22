# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/16 18:52
@Auth ： 异世の阿银
@File ：client2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver  # 网页驱动
from selenium.webdriver.common.by import By

'''
使用 selenium 查找 HTML 元素
'''


chrome_options = Options()
chrome_options.add_argument('--headless')       # 不显示浏览器
chrome_options.add_argument('--disable-gpu')    # 禁用gpu 图形界面gpu

# 创建一个 chrome 浏览器 驱动对象
driver = webdriver.Chrome(options=chrome_options)
# 发送请求
driver.get('http://127.0.0.1:5000')
# 获取页面数据
html = driver.page_source
# print(html)

# 查询元素与数据
# By.XPATH
try:
    # 需求: 查找h3
    element = driver.find_element(by=By.XPATH, value='//div[@class="info"]//h3')    # 不存在就报错
    # print(element.text)  # <selenium.webdriver.remote.webelement.WebElement
    # 需求: 查找所有的span # find_element() 匹配第一个满足条件的元素
    element = driver.find_element(by=By.XPATH, value='//div[@class="info"]//span')
    # print(element.text)
    # find_elements() 匹配所有满足条件的元素 返回列表数据类型
    elements = driver.find_elements(by=By.XPATH, value='//div[@class="mark"]//span')
    # for element in elements:
    #     print(element.text)
    # 需求: 查询手机图片路径
    element = driver.find_element(by=By.XPATH, value='//div[@class="pic"]/img')
    src = element.get_attribute('src')
    print(src)
    src = element.get_attribute('alt')  # alt 是 img 标签的属性, 但是此处的 img 没有 alt 属性, 程序不错误.
    src = element.get_attribute('xxx')  # xxx 不是 img 标签的属性, 返回结果为 None 对象.

    # 需求: 查找class="mark"的文本
    element = driver.find_element(by=By.XPATH, value='//div[@class="mark"]')
    innerHTML = element.get_attribute('innerHTML')
    print(f'innerHTML = {innerHTML}')
    print('-' * 100)
    outerHTML = element.get_attribute('outerHTML')
    print(f'outerHTML = {outerHTML}')
except BaseException as e:
    print(e)

# 查询元素与数据
# By.ID
# h3标签
element = driver.find_element(By.ID, value='title')
print(element.text)

# By.NAME
element = driver.find_element(By.NAME, value='mark')
print(element.text)

# By.CSS_SELECTOR
css_selector = 'div[class="info"] span[name="mark"]'
element = driver.find_element(By.CSS_SELECTOR, value=css_selector)
print(element.text)

css_selector = 'div[class="pic"] > img'
element = driver.find_element(By.CSS_SELECTOR, value=css_selector)
print(element.get_attribute('src'))

# 查找class = "mark" 下的所有元素
css_selector = 'div[class="mark"] *'
elements = driver.find_elements(By.CSS_SELECTOR, value=css_selector)
for element in elements:
    print(element.text)

# 查找 荣耀9i
css_selector = '#title'
element = driver.find_element(By.CSS_SELECTOR, value=css_selector)
print(element.text)

# 使用 tag name 标签名字查找
elements = driver.find_elements(By.TAG_NAME, value='span')
for element in elements:
    print(element.text)

# 查找手机型号
element = driver.find_element(By.TAG_NAME, value='h3')
print(element.text)


# 通过 class name 查找 所有class="pl"的所有元素
elements = driver.find_elements(By.CLASS_NAME, value='pl')
for element in elements:
    print(element.text)







# 关闭浏览器
driver.close()