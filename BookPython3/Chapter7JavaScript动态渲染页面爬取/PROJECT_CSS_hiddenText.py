# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROJECT_CSS_hiddenText.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/23 13:53 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

import re
import requests


# 用requests库读取结果，提取CSS， 通过睁着表达式将映射关系提取出来
url = 'https://antispider4.scrape.center/css/app.654ba59e.css'
response = requests.get(url)
pattern = re.compile('.icon-(.*?):before\{content:"(.*?)"\}')
results = re.findall(pattern, response.text)
print(results)
icon_map = {item[0]: item[1] for item in results}
print(icon_map['789'])
print(icon_map['981'])
print(icon_map['504'])


def parse_score(item):
    elements = item('.icon')
    icon_values = []
    for element in elements.items():
        class_name = (element.attr('class'))
        icon_key = re.search('icon-(\d+)', class_name).group(1)
        icon_value = icon_map.get(icon_key)
        icon_values.append(icon_value)
    return ''.join(icon_values)


browser = webdriver.Chrome()
browser.get('https://antispider4.scrape.center/')
WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
doc = pq(html)
items = doc('.item')
for item in items.items():
    name = item('.name').text()
    categories = [o.text() for o in item('.categories button').items()]
    # score = item('.score').text()
    score = parse_score(item)
    print(f'name: {name} categories: {categories} score: {score}')  # 不能获取评分
browser.close()





