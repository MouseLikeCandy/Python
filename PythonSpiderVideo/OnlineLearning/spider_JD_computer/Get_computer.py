# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/23 19:30
@Auth ： 异世の阿银
@File ：Get_computer.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


import requests
from lxml import etree
import xlwt

cookies = {
    '__jdv': '122270672|direct|-|none|-|1653305626329',
    '__jdu': '1653305626329952812430',
    'shshshfpa': 'be435e53-df91-5c30-ae69-aa4d29bba89b-1653305626',
    'shshshfpb': 'sDJaeal6rbU448qoKco0dPw',
    'areaId': '8',
    'ipLoc-djd': '8-560-50821-63241',
    '__jda': '122270672.1653305626329952812430.1653305626.1653305626.1653305626.1',
    '__jdc': '122270672',
    'shshshfp': '4d1eeddbb9f246c7be4af6a84e3f0ccc',
    'rkv': '1.0',
    '__jdb': '122270672.6.1653305626329952812430|1.1653305626',
    'shshshsID': '1d28105a507343091b0eff509b2880e3_6_1653305736829',
    'qrsc': '2',
    '3AB9D23F7A4B3C9B': 'RGP74RJ2IKDEYVPTUOLGXZONWGWIYH7D2TXTIF6BMJJLHOR5MT3G2XGFMCTNIOIYOCMFSQ7IVXOAXJALB56RG5FXLY',
}

headers = {
    'authority': 'search.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__jdv=122270672|direct|-|none|-|1653305626329; __jdu=1653305626329952812430; shshshfpa=be435e53-df91-5c30-ae69-aa4d29bba89b-1653305626; shshshfpb=sDJaeal6rbU448qoKco0dPw; areaId=8; ipLoc-djd=8-560-50821-63241; __jda=122270672.1653305626329952812430.1653305626.1653305626.1653305626.1; __jdc=122270672; shshshfp=4d1eeddbb9f246c7be4af6a84e3f0ccc; rkv=1.0; __jdb=122270672.6.1653305626329952812430|1.1653305626; shshshsID=1d28105a507343091b0eff509b2880e3_6_1653305736829; qrsc=2; 3AB9D23F7A4B3C9B=RGP74RJ2IKDEYVPTUOLGXZONWGWIYH7D2TXTIF6BMJJLHOR5MT3G2XGFMCTNIOIYOCMFSQ7IVXOAXJALB56RG5FXLY',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    'keyword': '显示器23.8',
}

response = requests.get('https://search.jd.com/Search', params=params, cookies=cookies, headers=headers)
html_data = response.text
# print(html_data)


wb = xlwt.Workbook()
lcd = wb.add_sheet('显示器价格')
title = ['名称', '价格']
for index in range(len(title)):
    lcd.write(0, index, title[index])
wb.save('显示器.xls')

doc = etree.HTML(response.content.decode('utf-8'))
for i in range(1, 30):
    href_url = doc.xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[1]/a/@href')
    # print(f'{href_url}, {type(href_url)}')
    for url in href_url:
        # print(f'url = {url}, {type(url+"")}')
        str_url = "https:" + url
        response2 = requests.get(str_url, params=params, cookies=cookies, headers=headers)
        html_data2 = response2.text
        doc2 = etree.HTML(html_data2)
        LCD_name = doc2.xpath('//div[@class="sku-name"]/text()')
        LCD_price = doc2.xpath('//div[@class="dd"]/span[@class="p-price"]')
        print(f'{LCD_name}, LCD_name:{type(LCD_name)}')
        print(f'{LCD_price}, LCD_price:{type(LCD_price)}')
        lcd.write(i, 0, LCD_name)
        wb.save('显示器.xls')
        lcd.write(i, 1, str(LCD_price[0]))
        wb.save('显示器.xls')

