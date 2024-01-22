# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/7 8:50
@Auth ： 异世の阿银
@File ：test09.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
    "四大天王:"
    歌神 - 张学友
    综合 - 刘德华
    舞王 - 郭富城
    文艺 - 黎明
    
    "四大美女:"
    沉鱼 - 西施浣纱
    落雁 - 昭君出塞
    闭月 - 貂蝉拜月
    羞花 - 贵妃醉酒
    
    "四大名捕:"
    冷血 - 邓超
    无情 - 刘亦菲
    铁手 - 皱兆龙
    追命 - 郑中基
'''

# 实现数据的存储和遍历
# 字典产生对应关系
# 格式: 字典嵌套字典 {'四大天王': {'歌神': 张学友, }, '四大美女': {}}

# 定义一个总字典
data_dict = {}
# 1.定义一个字典
king_of_pop = {'歌神': '张学友', '综合': '刘德华', '舞王': '郭富城', '文艺': '黎明'}
data_dict['四大天王'] = king_of_pop

beauty_of_girls = {'沉鱼': '西施浣纱', '落雁': '昭君出塞', '闭月': '貂蝉拜月', '羞花': '贵妃醉酒'}
data_dict['四大美女'] = beauty_of_girls

# 2.遍历数据
for title, data in data_dict.items():
    print(f'title = {title}')
    print(f'data = {data}')             # data是一个字典
    for nickname, name in data.items():         # for item in data:直接遍历字典,相当于遍历所有key
        print(f'{nickname} = {name}')

