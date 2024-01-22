'''
实时流媒体/伪流媒体
http/https
音频文件.acc文件
视频文件.H264     分割成 m3u8文件和ts文件
'''

# 1. 找ts文件
# Network   搜索.ts 小片段

# 2. 找m3u8文件
# Network   搜索.m3u8

# 3. 使用ffmpeg


import requests
import re
import os
# 'https://videozmwbf.0afaf5e.com/decry/vd/20231206/MzNlYzZkNzg2NjE0/144210/720/libx/hls/encrypt/MzNlYzZkNzg2NjE017.ts'
url_prifix = 'https://videozmwbf.0afaf5e.com/decry/vd/20231206/MzNlYzZkNzg2NjE0/144210/720/libx/hls/encrypt/MzNlYzZkNzg2NjE'
url = 'https://videozmwbf.0afaf5e.com/decry/vd/20231206/MzNlYzZkNzg2NjE0/144210/720/libx/hls/encrypt/index.m3u8'
res = requests.get(url).text
print(res)

ts = re.findall(r'(\d+).ts', res, flags=re.S)
print(ts)

ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
# 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
cookies = {
    '_ym_uid': '1683966165917727279',
    '_ym_d': '1683966165',
    '_ym_isad': '1',
    '_gid': 'GA1.2.391762671.1683966170',
    'https://ak21727.com/20230511/lkOgp63t/index.m3u8': '57.261336',
    'https://ak21727.com/20230512/8VTFwOF1/index.m3u8': '2054.537032',
    'https://ak21727.com/20230505/lu1XuNyC/index.m3u8': '39.930897',
    'https://ak21727.com/20230506/Mr4XPHEj/index.m3u8': '29.11352',
    'https://ak21727.com/20230506/zkiyBOHp/index.m3u8': '230.411848',
    '_ga_HJPBJDK82H': 'GS1.1.1683966169.1.1.1683968981.0.0.0',
    '_ga': 'GA1.1.575488742.1683966170',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://vip.aqdw126.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://vip.aqdw126.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.get(url, headers=headers)

for i in ts:
    u = url_prifix+i+".ts"
    r = requests.get(url=u, headers=headers).content
    print(i, u)
    s = '%d' %int(i)    # 整型转为字符串
    with open('./ts002/'+ s +'.ts', mode='wb') as file:
        file.write(r)
        cmd = "openssl aes-128-cbc -d -in ./ts002/" +s+ ".ts -out ./ts0022/0" +s+ ".ts -iv 00000000000000000000000000000000 -K  37613432633731363239396236663036"
        os.system(cmd)





