'''
京东
https://list.jd.com/list.html?cat=670%2C671%2C672&go=0 选择电脑-笔记本
https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91 搜索电脑
'''

from bs4 import BeautifulSoup
import requests

cookies = {
    'shshshfpa': '177a347e-2d5f-39ff-3410-56b96d267a2b-1566042224',
    'shshshfpb': 'r8jvx1mI763lihYZDDZtrkg%3D%3D',
    'TrackID': '1m43n4hpG3Esut2EZLhUZV46ZnI9nUjka5iyj-OrtpKRUgMhO78YDNqzH2zjOg_QWrd-HxXvFYPqEPKcSsLSqjUm2kKElXcqlFtrVqRWEz2Y',
    'unpl': 'JF8EAK1nNSttDB5UUUsHTBETSwkEWw0JTEdTbTQABA9QTlxSGlEfRhJ7XlVdXhRKEx9uYBRXXFNLXA4aBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrARsaGU9UUFteOHsQM19XDVddXktRNRoyGiJSHwFXVlsNTBRObGcNXVlRT1EGKwMrEQ',
    '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ed1ea4f221ea4a06aa3b4ac949f0b5e3|1651839307368',
    '__jdu': '219858542',
    'areaId': '8',
    'ipLoc-djd': '8-560-0-0',
    'PCSYCityID': 'CN_210000_210100_0',
    '__jda': '122270672.219858542.1651839306.1651839306.1651839307.1',
    '__jdc': '122270672',
    'shshshfp': '650f3bdf2e8e3888557cf9ea82988722',
    'rkv': '1.0',
    '__jdb': '122270672.6.219858542|1.1651839307',
    'shshshsID': '66bce6dd924cb840e3dc508f3cef62d6_4_1651839527288',
    'qrsc': '2',
    '3AB9D23F7A4B3C9B': 'SXYXAEZWWNM3RIE45FF42UQB622EC7C2RBF4ODD5PJAZNTHANQXDSP7NSUTDTQBMIMHLL4IY5QYUZKDTUC5LQRV4QQ',
}

headers = {
    'authority': 'search.jd.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'shshshfpa=177a347e-2d5f-39ff-3410-56b96d267a2b-1566042224; shshshfpb=r8jvx1mI763lihYZDDZtrkg%3D%3D; TrackID=1m43n4hpG3Esut2EZLhUZV46ZnI9nUjka5iyj-OrtpKRUgMhO78YDNqzH2zjOg_QWrd-HxXvFYPqEPKcSsLSqjUm2kKElXcqlFtrVqRWEz2Y; unpl=JF8EAK1nNSttDB5UUUsHTBETSwkEWw0JTEdTbTQABA9QTlxSGlEfRhJ7XlVdXhRKEx9uYBRXXFNLXA4aBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrARsaGU9UUFteOHsQM19XDVddXktRNRoyGiJSHwFXVlsNTBRObGcNXVlRT1EGKwMrEQ; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ed1ea4f221ea4a06aa3b4ac949f0b5e3|1651839307368; __jdu=219858542; areaId=8; ipLoc-djd=8-560-0-0; PCSYCityID=CN_210000_210100_0; __jda=122270672.219858542.1651839306.1651839306.1651839307.1; __jdc=122270672; shshshfp=650f3bdf2e8e3888557cf9ea82988722; rkv=1.0; __jdb=122270672.6.219858542|1.1651839307; shshshsID=66bce6dd924cb840e3dc508f3cef62d6_4_1651839527288; qrsc=2; 3AB9D23F7A4B3C9B=SXYXAEZWWNM3RIE45FF42UQB622EC7C2RBF4ODD5PJAZNTHANQXDSP7NSUTDTQBMIMHLL4IY5QYUZKDTUC5LQRV4QQ',
}

params = {
    'keyword': '电脑',
}
# 1、请求网络
response = requests.get('https://search.jd.com/Search', params=params, cookies=cookies, headers=headers)
# 打印
# print(f'response:{response}, response.text:{response.text}')

# 2、解析6种常用方式
# pip install bs4  # 本次使用BeautifulSoup
# 解析器 - 内置 -1、 lxml 2、html.parser 过滤 - 类似ctrl+f
soup = BeautifulSoup(response.text, 'html.parser')

for div in soup.find_all('div', class_='ml-wrap'):
    for div in soup.find_all('div', class_='goods-list-v2 gl-type-1 J-goods-list'):
        for div in soup.find_all('div', class_='p-price'):
            for price in soup.find_all('i'):
                # print(price)
                print(price.text)

'''
<i data-price="10043598885664">
2788.00
</i>
动态加载  - 1、滚轮滑块   2、 selenium




爬虫 - 数据分析 - 图形可视化 
hive分析
hadoop生态圈
大数据平台可视化

'''