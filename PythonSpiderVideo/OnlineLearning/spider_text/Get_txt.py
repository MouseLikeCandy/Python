# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/20 19:32
@Auth ： 异世の阿银
@File ：Get_txt.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests
from lxml import etree

response = requests.get("https://www.unjs.com/fanwenku/203701.html")
html_data = response.text
doc = etree.HTML(response.content.decode('gb2312'))
href_url = doc.xpath('//div[@class="content"]/p/text()')
print(href_url)

for item in href_url[1:]:  # 进行切片，默认是从零开始
    print(item)