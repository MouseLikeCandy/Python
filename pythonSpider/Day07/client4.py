# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 22:09
@Auth ： 异世の阿银
@File ：client1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""
get 与 post 混用
"""
import urllib.request
import urllib.parse

# 1.定义一个url请求地址
url = 'http://127.0.0.1:5000'

# 准备参数  汉字转为字节数据
province = urllib.parse.quote('广州')
city = urllib.parse.quote('深圳')
url = url + f'?province={province}&city={city}'   # get请求

# post数据
note = '''
深圳，简称“深”，别称鹏城，广东省辖地级市，是广东省副省级市，
国家计划单列市，超大城市，国务院批复确定的中国经济特区、全国性经济中心城市、国际化城市、 [1]  
科技创新中心、区域金融中心、商贸物流中心。 [207]  
全市下辖9个行政区和1个新区，总面积1997.47平方千米，建成区面积927.96平方千米。 [2-4]  
根据第七次人口普查数据，截至2020年11月1日零时，深圳市常住人口为1767.38万人。 [172]  [229]  
2021年，全市地区生产总值为30664.85亿元。 [214] 
'''

# data = 'note=' + urllib.parse.quote(note)   # data是字符串类型     以键值对的形式发送数据
# data = data.encode()   # data转换为字节数据

data = ('note=' + urllib.parse.quote(note)).encode()    # 合并写法

# 2.发送请求, 获取相应          # 同一个请求中, 实现了get与post请求数据的和并提交
response = urllib.request.urlopen(url, data)    # 两个参数  url是get数据, data是post数据

# 3.解析数据
data = response.read().decode()     # 默认编码为utf-8
print(data)

