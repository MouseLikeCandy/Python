"""
 爬虫
 1、网络请求-从网页获取数据
 2、提取数据
 3、保存-持久化

"""

from wordcloud import WordCloud as wc
import wordcloud  # 词云图
import requests  # 网络请求

cookies = {
    'tvfe_boss_uuid': '7bed7f82e8dc9ac4',
    'pgv_pvid': '8896137929',
    'video_guid': '716410cc4cd5e94e',
    'video_platform': '2',
    'pgv_pvi': '7657232384',
    'RK': 'XGjphF88Rj',
    'ptcz': '793d33cc44a49745ef0f7b65c1584c8bc020b567d351412ab06c2979820e2215',
    'o_cookie': '247240467',
    'pac_uid': '1_247240467',
    'pgv_info': 'ssid=s5873109618',
    'vversion_name': '8.2.95',
    'video_omgid': '716410cc4cd5e94e',
}

headers = {
    'authority': 'mfm.video.qq.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://v.qq.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'tvfe_boss_uuid=7bed7f82e8dc9ac4; pgv_pvid=8896137929; video_guid=716410cc4cd5e94e; video_platform=2; pgv_pvi=7657232384; RK=XGjphF88Rj; ptcz=793d33cc44a49745ef0f7b65c1584c8bc020b567d351412ab06c2979820e2215; o_cookie=247240467; pac_uid=1_247240467; pgv_info=ssid=s5873109618; vversion_name=8.2.95; video_omgid=716410cc4cd5e94e',
}

params = {
    'otype': 'json',
    #'callback': 'jQuery19109074419909910831_1650892299133',  # 注释掉
    'target_id': '1227342321&vid=r0018hmh1pa',
    'session_key': '0,0,0',
    'timestamp': '15',
    '_': '1650892299159',
}

response = requests.get('https://mfm.video.qq.com/danmu', params=params, cookies=cookies, headers=headers)


print(f'response:{response}, type: {type(response)}')
print(response.json())
file = open('WordCloud_danmu.txt', 'w', encoding="utf-8")
wc = wordcloud.WordCloud(background_color='white',
                         font_path='C:\\Windows\\Fonts\\MSYH.TTC',
                         width=3000,
                         height=3000,
                         )
for i in response.json()['comments']:
#    print(i)

    for text in i['content']:
        print(text, end='')


#        file.write(text)   # 一行了需要配合换行
    file.write(i['content'] + '\n')
file.close()
# 打开文本
with open(r'WordCloud_danmu.txt', 'r+', encoding="UTF-8") as f:
    s = f.read()

    wg = wc.generate(s)
    wg.to_file('WordCloud_danmu.jpg')
#    print(help(wg))
# 每30s更一次弹幕300个，
