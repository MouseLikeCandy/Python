# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROJECT_SELENIUM.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/23 9:28 
"""
import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import logging

from urllib.parse import urljoin

from os import makedirs
from os.path import exists


RESULTS_DIR = 'Project_selenium_results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")  # 日志

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10       # 超时时间
TOTAL_PAGE = 10     # 总页数

browser = webdriver.Chrome()
wait = WebDriverWait(browser, TIME_OUT)


# 通用爬取方法：对任意URL进行爬取
def scrape_page(url, condition, locator):
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


# 爬取列表页
def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


# 解析列表页
def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


# 爬取详情页
def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_element_located, locator=(By.TAG_NAME, 'h2'))


# 解析详情页
def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.TAG_NAME, 'h2').text
    categories = [element.text for element in browser.find_elements(By.CSS_SELECTOR, '.categories button span')]
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    score = browser.find_element(By.CLASS_NAME, 'score').text
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


# 数据存储
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# main方法，串联所有的方法, 得到所有详情页的URL
def main():
    try:
        for page in range(1, TOTAL_PAGE+1):
            scrape_index(page)
            detail_urls = parse_index()
            # logging.info('detail urls %s', list(detail_urls))
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                logging.info('detail data %s', detail_data)
                save_data(detail_data)
    finally:
        browser.close()


if __name__ == '__main__':
    main()