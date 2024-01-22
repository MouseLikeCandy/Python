# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/3 8:49
@Auth ： 异世の阿银
@File ：GetDanmu.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""
爬虫三步：
1、请求数据  
腾讯视频  长津湖之水门桥 
网页内容抓包工具 F12  刷新   Network  danmu   copy as cUrl
粘贴到 https://curlconverter.com/#python 生成Python代码
# params中参数需要删去或者注释掉 #'callback': 'jQuery19108252156772927515_1651549978150',   
不然会报错json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
2、提取数据
3、保存数据
"""
#  pip install --target=d:\python3.7.3\lib\site-packages wordcloud -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
import requests
import wordcloud
cookies = {
    'tvfe_boss_uuid': 'f6d85bb2622e8237',
    'video_platform': '2',
    'pgv_pvid': '7291950778',
    'pgv_info': 'ssid=s9542255340',
    'video_guid': '97ab55ca320b133564312eb4ea31da1d',
    'vversion_name': '8.2.95',
    'video_omgid': '97ab55ca320b133564312eb4ea31da1d',
}

headers = {
    'authority': 'mfm.video.qq.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'tvfe_boss_uuid=f6d85bb2622e8237; video_platform=2; pgv_pvid=7291950778; pgv_info=ssid=s9542255340; video_guid=97ab55ca320b133564312eb4ea31da1d; vversion_name=8.2.95; video_omgid=97ab55ca320b133564312eb4ea31da1d',
    'referer': 'https://v.qq.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    'otype': 'json',
#    'callback': 'jQuery191009916179937543279_1651544155950',
    'target_id': '7795611565&vid=a0042ytu9lv',
    'session_key': '0,855,1651544156',
    'timestamp': '45',
    '_': '1651544155973',
}

response = requests.get('https://mfm.video.qq.com/danmu', params=params, cookies=cookies, headers=headers)

print(f'response:{response}, type:{type(response)}')  # 200 正常响应

print(f'json数据：{response.json()}')  # 查看数据 字典类型 找到需要的弹幕信息 content
print('-' * 100)
# 字典类型 一层一层进入
print(f'response.json()的键：')
for key in response.json():
    print(key, end=' ')

print(f'response.json()[comments]的内容：')
print(response.json()['comments'])

# 得到的内容保存到文本文件
file = open(f'E:\\PythonProject\\OnlineLearning\\spider_danmu\\长津湖之水门桥.txt', 'w', encoding='utf-8')
for comment in response.json()['comments']:
    print(f"{comment['opername']}: {comment['content']}")
#    print(f'response.json()[comments]列表中的每个字典：')
#    for key in comment:
#        print(key, end=' ')
    file.write(comment['content']+'\n')
file.close()

# 词云图
wc = wordcloud.WordCloud(background_color='white', #None
                         font_path='C:\\Windows\\Fonts\\MSYH.TTC',
                         width=1920,
                         height=1080)
# 打开文本
path = 'E:\\PythonProject\\OnlineLearning\\spider_danmu\\长津湖之水门桥.txt'
with open(path, 'r+', encoding='UTF-8') as f:
    s = f.read()
wg = wc.generate(s)
wg.to_file('长津湖之水门桥.jpg')


# 背景词云图
from wordcloud import WordCloud  # 词云库
import matplotlib.pyplot as plt  # 数学绘图库
import numpy as np
from PIL import Image
mask = np.array(Image.open("心.png"))
wc1 = WordCloud(
    background_color="white",  # 背景为白色
    font_path='F:\\simfang.ttf',  # 使用的字体库:当前字体支持中文
#    max_words=20,  # 最大显示的关键词数量
    width=1400,  # 生成词云的宽
    height=768,  # 生成词云的高
    collocations=False,  # 解决关键词重复：是否包括两个词的搭配
    mask=mask,
    # stopwords=STOPWORDS, #屏蔽的内容
    mode='RGBA'
)
with open(path, 'r', encoding='UTF-8') as f:
    text = f.read()
wc2 = wc1.generate(text)

plt.imshow(wc2)
plt.axis("off")
plt.savefig('生成的词云.jpg', dpi=600, bbox_inches='tight')
plt.show()



