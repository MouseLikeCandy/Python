# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/14 13:12
@Auth ： 异世の阿银
@File ：GetVipMp4.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


'''
# 打开一个VIP视频  F12   搜索.ts文件（视频小片段）/ .m3u8    
'''
#'https://btrace.video.qq.com/kvcollect?BossId=4501&Pwd=142347456&hc_main_login=&hc_vuserid=&hc_openid=&hc_appid=&loginid=&loginex=&logintype=0&guid=2579d5b588744e8a07f2cb363ee892d1&longitude=&latitude=&vip=0&online=1&p2p=1&downloadkit=1&resolution=1920*1080*1&testid=&osver=windows+10.0&playerver=&playertype=1&uip=182.200.10.170&confid=&cdnip=&cdnid=2805&cdnuip=&freetype=&sstrength=&network=&speed=&device=&appver=3.5.57&p2pver=5.2.51&url=https://v.qq.com/x/cover/mcv8hkc8zk8lnov/o0042xfyy4u.html&refer=https://v.qq.com/&ua=Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML++like+Gecko)+Chrome/100.0.4896.127+Safari/537.36&ptag=www_baidu_com|videolist:click&flowid=d4933f38bbb322fcfe8a2f2639b387a4_10201&platform=10201&dltype=3&vid=o0042xfyy4u&cid=mcv8hkc8zk8lnov&fmt=321002&rate=106&clip=4&status=8&type=1030&duration=1243.93&ext={"dltype":3,"m3u8":0}&drm=0&proto=tcp&protover=tcp00&data={"stime":1652505028960,"etime":1652505029458,"p2p_ctime":136,"p2p_pretime":118,"bufferduration":"","vt":2805,"url":"https://apd-adc32fe0d6a6530de3c7e8670884b46f.v.smtcdns.com/vipts.tc.qq.com/AKTwNKnnx1cLhkaUyMDTLUjsbKJS4y_S6xTDwNowUfgo/uwMROfz2r57AoaQXGdGnC2de6448_15NlFLR-6JgreBXkPz2/svp_50112/MwPgIKtQanyWsnv4kJ_BGS4Rd6KGDsjBWsZGP7pBYhL9ZSLb61BkpGA4p8xJxdawYmZdWKc6ieSkg8yU9T_SmFpNkWOf88vu6mNYdnBhadwQVJNh71B-Cu86M9fCHgZ4eJXWAhx4LwmlxIDjhwed8vJ_JV-22yTZKRPKUXERt_mlKsP_dTj2bw/0325_gzc_1000102_0b53lqaaoaaatiaknwltmfrmaxgda5naaa2a.f321002.ts.m3u8?ver=4","urlindex":0,"quic":0,"quicver":"","code":""}&step=30&seq=3'
# https://apd-adc32fe0d6a6530de3c7e8670884b46f.v.smtcdns.com/vipts.tc.qq.com/AKTwNKnnx1cLhkaUyMDTLUjsbKJS4y_S6xTDwNowUfgo/uwMROfz2r57AoaQXGdGnC2de6448_15NlFLR-6JgreBXkPz2/svp_50112/MwPgIKtQanyWsnv4kJ_BGS4Rd6KGDsjBWsZGP7pBYhL9ZSLb61BkpGA4p8xJxdawYmZdWKc6ieSkg8yU9T_SmFpNkWOf88vu6mNYdnBhadwQVJNh71B-Cu86M9fCHgZ4eJXWAhx4LwmlxIDjhwed8vJ_JV-22yTZKRPKUXERt_mlKsP_dTj2bw/0325_gzc_1000102_0b53lqaaoaaatiaknwltmfrmaxgda5naaa2a.f321002.ts.m3u8?ver=4


# 加密的m3u8要怎么解密？

'''
第一个m3u8还算正常，之后的都是加密的
https://apd-ad181a347e49aea1bbdb944dbe516b42.v.smtcdns.com/vipts.tc.qq.com/AGTEUOSfCHinuqaf06HoiXUs1f2ZXzzmM8T-646Wi63A/uwMROfz2r57AoaQXGdGnC2de6448_15NlFLR-6JgreBXkPz2/svp_50112/XNRBtOYze97AYNhtUBvJ7OmQeoUnKTwIcd8cVPtMP8p9LvZDgpX3yTMcerKaWDZbtq4ozcstXfmtR0NaZg_q1c-Gr3gkuOulJN1-0Q5mptuFQ604iUCJFiyFM-XWVpoSPYFCsLLATBoAc-2kiHFfa_nQRQT_2kmP0F5mA6quBoJhFqEqlnm28A/0385_gzc_1000102_0b53bmaaaaaaeiadmedzxfrmac6daadqabca.f321002.ts.m3u8?ver=4
ffmpeg -i 'm3u8' -acodec copy -vcodec copy zuizhong.mp4


腾讯VIP视频能够获取免费的6分钟
'''