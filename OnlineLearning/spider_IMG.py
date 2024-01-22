

import requests

cookies = {
    'Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273': '1650975227',
    'Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273': '1650975227',
}

headers = {
    'authority': 'www.tupianzj.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1650975227; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1650975227',
    'if-none-match': 'W/"62191066-7f28"',
    'if-modified-since': 'Fri, 25 Feb 2022 17:22:46 GMT',
}
# 第一步发起网络请求
response = requests.get('https://www.tupianzj.com/meinv/mm/meizitu/')
#print(response.text)
# 解码
print(response.content.decode('gb2312'))
# 解析模块  -xpath 工具
# //*[@id='container']/div/div/div[2]/div[2]/
