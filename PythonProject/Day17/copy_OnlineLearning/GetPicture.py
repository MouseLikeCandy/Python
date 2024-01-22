'''
爬虫三步曲
1、目标 - 分析  -发起网络请求   - 得到数据
https://www.tupianzj.com/meinv/mm/meizitu/
https://www.tupianzj.com/meinv/mm/taiwanmei/  专题
详情页的网址37页   - 抓小图 or 抓大图
https://www.tupianzj.com/meinv/20190319/182972.html
https://www.tupianzj.com/meinv/20190319/182972_8.html
https://www.tupianzj.com/meinv/20190319/182972_20.html

F12 抓包工具 - 快捷键 - 监控
刷新页面加载数据   network  找到与当前目标一致的  copy  as cURL
粘贴到工具里 Convert curl commands to Code(Python)  生成代码
2、提取数据  - 取其精华去其糟粕
3、保存 - 持久化保存
'''


# pip install requests  -i https://pypi.douban.com/simple  豆瓣镜像

from lxml import etree
import requests
import time
import os

cookies = {
    'Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273': '1650980983',
    'Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273': '1650981023',
}

headers = {
    'authority': 'www.tupianzj.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1650980983; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1650981023',
    'if-modified-since': 'Fri, 25 Feb 2022 17:22:46 GMT',
    'if-none-match': 'W/"62191066-7f28"',
    'referer': 'https://www.baidu.com/link?url=xjq_jAlNPNFnnD7VZeN2HdstymKBYCAuvU9_gYfj3Y2Jf6NF9Hd4Z9ylj9ZnMPyGAXNoa5purLIHJejUAcnSW_&wd=&eqid=afa19e3b000147a0000000036267f871',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}
# 第一步；发起网络请求
# response = requests.get('https://www.tupianzj.com/meinv/mm/meizitu/', cookies=cookies, headers=headers)
response = requests.get('https://www.tupianzj.com/meinv/mm/meizitu/')

# print(response.text)
# 发现有乱码，找到输出中包含了编码方式 charset=gb2312
# 或者在网站上右键 - 查看网页源代码 - charset=gb2312

# 转码  content 获取网址内容的二进制 decode 解码
# print(response.content.decode('gb2312'))

# 解析模块 - xpath
# xpath 工具语法
# //*[@id="container"]/div/div/div[2]/div[2]/div[2]/dl/dd/ul/li[4]/a/@href
# // 根目录       从左往右的第一个标签都是根目录
# [] 判断的条件
# @ 提取数据
# / 往下找数据
# //ul[@class="d1 ico3"]/li/a/@href

# 环境配置
# from lxml import etree  解析模块

# 加载数据
doc = etree.HTML(response.content.decode('gb2312'))

href_url = doc.xpath('//ul[@class="d1 ico3"]/li/a/@href')
# print(f'href_url:{href_url}, type: {type(href_url)}')
# 找到了页面所有值 --下一步拼接
# 第一个是不需要的'/meinv/mm/meizitu/'
for item in href_url[1:]:  # 进行切片，默认是从零开始
    url = 'https://www.tupianzj.com'+item
#    print(url)
# 变成了每一组图片的详情页
# 需要取得详情页里面的每张图
# 再发请求
#    pic_url = requests.get(url).content.decode('gb2312') # 前端后台不一致
# 后端接口数据修改了
    pic_all_url = requests.get(url).content.decode('gbk')
#    print(f'pic_all_url:{pic_all_url}, type: {type(pic_all_url)}')
    # 分析网址
    # https: // www.tupianzj.com / meinv / 20190319 / 182972.html
    # https: // www.tupianzj.com / meinv / 20190319 / 182972_8.html
    # https: // www.tupianzj.com / meinv / 20190319 / 182972_20.html

    # 提取出共 _ 页，动态加载
    # xpath定位 //div[@class="pages"]/ul/li[1]/a/text()
    docs = etree.HTML(pic_all_url)
#    text_pages = docs.xpath('//div[@class="pages"]/ul/li[1]/a/text()')
    # replace() 或 正则 等
    text_pages = docs.xpath('//div[@class="pages"]/ul/li[1]/a/text()')[0].split('共')[1].split('页')[0]
#    print(text_pages)


    # 得到每一个详情页的页数 - 字符串
    for page in range(1, int(text_pages)+1):
        if page == 1:
            pic_img_url = url.split('.html')[0] + f'.html'
        else:
            pic_img_url = url.split('.html')[0]+f'_{page}.html'
#        print(f'pic_img_url:{pic_img_url}, type: {type(pic_img_url)}')

        # 做判断 下载图片 - 先找到该网址中图片的位置
        # //div[@id="bigpic"]/a/img/@src
        # 流文件下载原图
        pic_src_url = requests.get(pic_img_url).content.decode('gbk')
#        print(f'pic_src_url:{pic_src_url}, type: {type(pic_src_url)}')
        docs1 = etree.HTML(pic_src_url)
        pic_src = docs1.xpath('//div[@id="bigpic"]/a/img/@src')
        pic_text = docs1.xpath('//div[@id="bigpic"]/a/img/@alt')
#        print(f'pic_src:{pic_src}, type: {type(pic_src)}')
#        print(f'pic_src[0]:{pic_src[0]}, type: {type(pic_src[0])}')
#        print(f'pic_text:{pic_text}, type: {type(pic_text)}')
#        print(f'pic_text[0]:{pic_text[0]}, type: {type(pic_text[0])}')
        for pic in pic_src:
            pic_img = ''+pic
        for text in pic_text:
            pic_img_text = ''+text

# # 持久化   保存图片
        response = requests.get(pic_img, headers=headers)
        pic = response.content
#
        if not os.path.exists(pic_img_text):
            os.mkdir(pic_img_text)
#            os.chdir(pic_img_text)
        try:
            with open(f'{pic_img_text}/{pic_img_text}{page}.jpg', 'wb') as f:
                f.write(pic)
            time.sleep(1)
        except TypeError as e:
            print(f'下载出现异常{e}, 下载失败！')
        else:
            print(f'{pic_img_text}/{pic_img_text}{page}.jpg-----下载成功')



# 来自网络
'''
        r = requests.get(pic_src, headers=headers)  # 下载图片，之后保存到文件
        with open('pic/{}/{}'.format(pic_text, pic_text), 'wb') as f:
            f.write(r.content)
        time.sleep(1)  # 休息一下，不要给网站太大压力，避免被封
'''