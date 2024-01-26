# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PROJECT_OCR_tesserocr.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/23 17:15 
"""
import time
import re
import tesserocr
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from io import BytesIO
from PIL import Image
from retrying import retry
import numpy as np


# 图像预处理
def preprocess(image):
    image = image.convert('L')
    array = np.array(image)
    array = np.where(array > 50, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    return image


# 登录
@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    browser.get('https://captcha7.scrape.center/')
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    image = preprocess(image)
    captcha = tesserocr.image_to_text(image)
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(captcha)
    browser.find_element(By.CSS_SELECTOR, '.login').click()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(.,"登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False


if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()