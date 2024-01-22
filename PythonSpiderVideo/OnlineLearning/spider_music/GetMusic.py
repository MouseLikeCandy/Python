# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/4 21:33
@Auth ： 异世の阿银
@File ：GetMusic.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
目标：爬取网易云音乐 
爬虫三步曲：
火狐浏览器    
##什么是直链和外链？##
外链转换工具：https://link.hhtjim.com/按照示例格式进行转换
网易云音乐网址：https://music.163.com/#/song?id=441491828 水星记
外链转换后：https://link.hhtjim.com/163/441491828.mp3 在网址中可以直接打开播放
在网址中粘贴后的播放页：
https://m701.music.126.net/20220504221427/ac40db566d9d50de2360b3381ddb0342/
jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14096418064/
eabf/4b08/3f90/3a4eeeebf753ddcab37c3143ce69526e.mp3?bitrate=128000
直链工具：https://music.liuzhijin.cn/
网易云音乐网址：https://music.163.com/#/song?id=1217823
直链转换后：http://music.163.com/song/media/outer/url?id=1217823.mp3
'''


#//div[@class="txt"]/a/@href   xpath工具显示NULL

import requests
from lxml import etree
# 将列表格式的字符串转为列表格式
import ast
import json
import time

import os
# 浏览器渲染界面和需要的不一样
# response = requests.get("https://music.163.com/#/discover/toplist")
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
response = requests.get("https://music.163.com/discover/toplist", headers=ua)
html_data = response.text
# print(f'html_data:{html_data}, type:{type(html_data)}')
doc = etree.HTML(response.text)
href_url = doc.xpath('//ul[@class="f-hide"]/li/a/@href')
music_names = doc.xpath('//ul[@class="f-hide"]/li/a/text()')
music_infos = doc.xpath('//textarea[@id="song-list-pre-data"]/text()')
# print(f'href_url:{href_url}, href_url type:{type(href_url)}')
# print(f'music_names:{music_names}, music_names type:{type(music_names)}')
# print(f'music_infos:{music_infos}, music_infos type:{type(music_infos)}')



list_music = []
for music_info in music_infos:
#    print(f'music_info:{music_info}, music_info type:{type(music_info+"")}')  # 字符串
    str_music = music_info + ""
    # list_music = ast.literal_eval(str_music)
    list_music = json.loads(str_music)

# 创建文件夹
isExists = os.path.exists('download')
if not isExists:
    os.makedirs('download')

for music in list_music:
#    print(music, end='\n')  # 得到字典类型的music
#    print(music['name'], music['id'])
    url = f"http://music.163.com/song/media/outer/url?id={music['id']}.mp3"
    print(url)

    # 保存
    try:
        time.sleep(1)
        response = requests.get(url)
        with open(f"download\\{music['name']}.mp3", 'wb') as f:
            f.write(response.content)
        f.close()
    except:
        continue


# 下载后试听 - VIP音乐下载后听不了？或者是没有下成功，特殊字符的语言的都可以
# VIP音乐怎么下载呢？
# 对比？

