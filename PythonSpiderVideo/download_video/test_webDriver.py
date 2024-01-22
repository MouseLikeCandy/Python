# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：test_webDriver.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/12/21 9:33 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 Chrome 驱动的路径
# driver_path = r'C:\Program Files\chrome-headless-shell-win64\chrome-headless-shell.exe'
# driver = webdriver.Chrome(chromedriver_path)
# 新版本不需要填写地址，不然会报错

# 浏览器启动选项
options = webdriver.ChromeOptions()
options.add_argument('User-Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"')

# 创建 Chrome WebDriver
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get('https://www.damidm.com/player/2375-1-1.html')

# 等待页面加载完成，超时时间为10秒
wait = WebDriverWait(driver, 10)  # 设置显式等待
# element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="your_element_id"]')))

# 获取完整页面信息
full_page_html = driver.page_source

# 关闭浏览器窗口
driver.quit()

# 处理 full_page_html，获取你需要的信息
print(full_page_html)
