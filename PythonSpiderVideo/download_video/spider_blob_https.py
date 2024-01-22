# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：spider_blob_https.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/12/18 16:47 
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


main_url = "https://www.damidm.com/yhdm/2375.html"      # 主页
episode_url = "https://www.damidm.com/player/2375-1-1.html"     # 第141集
encode_url = "https://play.damidm.com/yun/?url=yinghua_91a1Mqk0Wy_Lywh1D__01EmNNlt4qUPKCTMwDek-WkltNhbVxLlBebP9wrn9YKk_Gxp14Iq5tVcjxe5huvu7O9VgYrZtOQ&next=https://www.damidm.com/player/2375-1-2.html&title=%E5%AE%8C%E7%BE%8E%E4%B8%96%E7%95%8C%E7%AC%AC141%E9%9B%86%E8%A7%86%E9%A2%91%E9%AB%98%E6%B8%85%E5%9C%A8%E7%BA%BF%E8%A7%82%E7%9C%8B"
decode_url = "https://play.damidm.com/yun/?url=yinghua_91a1Mqk0Wy_Lywh1D__01EmNNlt4qUPKCTMwDek-WkltNhbVxLlBebP9wrn9YKk_Gxp14Iq5tVcjxe5huvu7O9VgYrZtOQ&next=https://www.damidm.com/player/2375-1-2.html&title=完美世界第141集视频高清在线观看"
headers = {
"Referer": "https://play.damidm.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

# 浏览器启动选项
options = webdriver.ChromeOptions()
options.add_argument('User-Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"')
options.add_argument('Referer = "https://play.damidm.com/"')

# 创建 Chrome WebDriver
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get(episode_url)

# 设置显示等待
wait = WebDriverWait(driver, 10)  # 设置显式等待时间为10秒钟
# element = wait.until(EC.title_contains("iframe"))  # 等待页面标题包含特定关键字


# 获取嵌套在 <iframe> 中的 #document 内容
# 定位 iframe 元素
iframe_element = driver.find_element(By.XPATH, '//*[@id="playleft"]/iframe')  # 根据实际情况修改 XPath
# //*[@id="playleft"]/iframe

# 切换到 iframe 内部
driver.switch_to.frame(iframe_element)

# 获取 #document 内容
document_content = driver.page_source

# 切回主文档
driver.switch_to.default_content()

# 输出 #document 内容
print(document_content)
logger.warning("-" * 100)
# 获取完整页面信息
# full_page_html = driver.page_source
# 执行 JavaScript 代码，获取整个页面的 HTML 源代码
full_page_html = driver.execute_script("return document.documentElement.outerHTML;")

# 关闭浏览器窗口
driver.quit()

# 处理 full_page_html，获取你需要的信息
logger.info(full_page_html)


# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(full_page_html, 'html.parser')

# 找到所有的 <iframe> 标签
all_iframe_tags = soup.find_all('iframe')
logger.info(all_iframe_tags)

# 提取每个 <iframe> 标签的 src 属性值
for iframe_tag in all_iframe_tags:
    src_value = iframe_tag.get('src')
    logger.success(src_value)

# 找到所有的 <video> 标签
all_video_tags = soup.find_all('video')
logger.info(all_video_tags)

# 提取每个 <video> 标签的 src 属性值
for video_tag in all_video_tags:
    src_value = video_tag.get('src')
    logger.success(src_value)


