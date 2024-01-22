# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/12 7:01
@Auth ： 异世の阿银
@File ：GetMp4.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


''' 网站 - 猫眼电影 - 热点 - 预告片
https://www.maoyan.com/news?showTab=3
1、请求url   2、筛选数据，做好防反爬   3、得到MP4保存
'''

import requests
from lxml import etree

import re
'''
单个的视频网址 -- 右键 检查/F12 打开抓包工具 -- NetWork -- ALL -- 寻找.mp4文件 -- 选中 
-- request url:https://vod.pipi.cn/fec9203cvodtransbj1251246104/7bed426e387702300644912746/v.f42905.mp4即为视频地址
点击抓包工具左上角箭头 -- 点击网页视频 -- 弹出在前端代码elements下的视频位置   
-- <source src="https://vod.pipi.cn/fec9203cvodtransbj1251246104/7bed426e387702300644912746/v.f42905.mp4" type="video/mp4">

# 通过点击不同的小视频可以得到不同的网址，可以找到规律
http://imovie.pipi.cn/films/1299144/preview?videoId=487272
http://imovie.pipi.cn/films/1424470/preview?videoId=487232
http://imovie.pipi.cn/films/1348468/preview?videoId=487179


# 网址直接是一个视频地址
url = 'https://vod.pipi.cn/fec9203cvodtransbj1251246104/dd3dffc4387702300642705621/v.f42905.mp4'
response = requests.get(url)
with open('夺宝联盟.mp4','wb') as f:
    f.write(response.content)
'''

# 网址里面有许多视频，需要筛选出视频地址
url = 'https://www.maoyan.com/news?showTab=3&offset=80'
# 504 Gateway Time-out 504超时 反爬机制1 -- 添加UA User-Agent   Network下 随便点击一个数据包
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
# 猫眼验证中心 -- 滑块验证码 -- 手动划一下
#
cookie = {'Cookie':'uuid_n_v=v1; uuid=F75B8F20D17E11EC9BC33FFCCADBB20BCE521B37BD4E4388A8FA0E85C854C00C; '
          '_lxsdk_cuid=180b55f8f3bc8-0d3c261fb53741-6b3e555b-1fa400-180b55f8f3bc8; '
          '_lxsdk=F75B8F20D17E11EC9BC33FFCCADBB20BCE521B37BD4E4388A8FA0E85C854C00C; '
          '_lx_utm=utm_source=Baidu&utm_medium=organic; '
          '_csrf=9c8643bc369c1e00cdb954ffbc283ae7cc0ba94ab221dc43b8c35eb04b81156c; '
          'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1652310380,1652490493; '
          'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1652490886; '
          '__mta=217939881.1652310380372.1652490879705.1652490886257.13; '
          '_lxsdk_s=180c0c79577-4e9-136-bd6||1'}
response = requests.get(url, headers=ua)
# 得到网页数据 -- 字符串格式
html_str = response.text
print(html_str)
#  字符串格式 -- HTML格式 -- xpath工具只能筛选标签类型HTML、XML格式
html_dom = etree.HTML(html_str)
# list_url = html_dom.xpath('//div[@class="video-box"]/a/@href')  # 不用这个是因为里面没有电影名字
movie_urls = html_dom.xpath('//h4/a/@href')
movie_names = html_dom.xpath('//h4/a/text()')
for movie_name, movie_url in zip(movie_names, movie_urls):
    print(movie_name)
    print(movie_url)
    # 别忘记添加UA，还需要添加cookie
    movie_url_str = requests.get(movie_url, headers=ua, cookies=cookie).text
    print(movie_url_str)
    # 数据筛选 -- 正则
    # <source src="https://vod.pipi.cn/fec9203cvodtransbj1251246104/1b0addcc387702300249285614/v.f42905.mp4" type="video/mp4" />
    # 筛选条件：source src="(.*?)" type
    mp4_url = re.search('source src="(.*?)" type', movie_url_str).group(1)
    mp4 = requests.get(mp4_url, headers=ua).content
    with open(f'{movie_name}.mp4', 'wb') as file:
        file.write(mp4)


# 其他页连续下载
# https://www.maoyan.com/news?showTab=3&offset=80 第5页
# https://www.maoyan.com/news?showTab=3&offset=96 第7页



