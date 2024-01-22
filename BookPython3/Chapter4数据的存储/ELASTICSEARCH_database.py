# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：ELASTICSEARCH_database.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/9 14:45 
"""
from elasticsearch import Elasticsearch

# es = Elasticsearch(
#     ['https://[username:password@]hostname:port'],
#     verify_certs=True,  # 是否验证SSL证书
# )

# Elasticsearch 服务器地址
hosts = ["https://elastic:123456@localhost:9200"]

# es = Elasticsearch(hosts=hosts, verify_certs=False)
# 创建 Elasticsearch 客户端
client = Elasticsearch(
    hosts=hosts,
    # timeout=30,
    # DeprecationWarning: The 'timeout' parameter is deprecated in favor of 'request_timeout' 'timeout'参数已被弃用
    request_timeout=30,
    max_retries=3,  # 设置最大重试次数为3次
    verify_certs=True,  # 启用证书验证
    ca_certs=r"C:\elasticsearch-8.11.3\config\certs\http_ca.crt"  # 设置 CA 证书文件路径
)
print("成功地连接到 Elasticsearch 8.x", client)

INDEX_NAME = 'news'

e1 = {
    "first_name": "nitin",
    "last_name": "panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports', 'music'],
}

res = client.index(index=INDEX_NAME, document=e1)
print(res)

# 设置传输选项
transport_options = {
    'max_retries': 3,  # 例如，设置最大重试次数
    'retry_on_timeout': True  # 设置超时时是否重试
}

# 使用 Elasticsearch.options() 方法来设置传输选项
# client.options(ignore_status=[400, 404]).indices.delete(index='news')       # 删除索引
result = client.options(ignore_status=400).indices.create(index='news')     # 创建索引
print(result)
client.transport.close()


# 重新创建连接
ca_certs = r"C:\elasticsearch-8.11.3\config\certs\http_ca.crt"
client = Elasticsearch(hosts=hosts, verify_certs=True, ca_certs=ca_certs)
# client.options().indices.create(index='olds2')    # 创建索引

data = {
    'title': '乘风破浪不负韶华， 奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200'
}

# 使用create方法来插入数据需要指定id
# result = client.options().create(index='olds', id=16, body=data)
# print(result)
# result = client.options().create(index='olds', id=17, document=data)
# print(result)
# 使用index方法来插入数据自动生成id
result = client.index(index='olds', document=data)
print(result)

data = {
    'title': '乘风破浪不负韶华， 奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    'date': '2024-01-10',
    'phone': '13130227102',
    'street': '文溯街'
}

# 插入/更新数据
result = client.index(index='news', document=data, id=1)
# 更新数据
result = client.update(index='news', id=1, doc=data)
print(result)   # '_version': 2 之前修改过， result: 'noop' no operation  未操作

# 删除数据
result = client.delete(index='news', id=1)
print(result)
client.close()

#########################################
# 手动安装elasticsearch-analysis-ik, 然后重启elasticsearch
client = Elasticsearch("https://elastic:123456@localhost:9200", verify_certs=True, ca_certs=ca_certs)

mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}

client.indices.delete(index='news')
client.indices.create(index='news')
result = client.indices.put_mapping(index='news', body=mapping)
print(result)


# 插入几条数据
datas = [
    {
        'title': '高考结局大不同',
        'url': 'https://k.sina.com.cn/article_7571064628_1c3457340001011lz9.html'
    },
    {
        'title': '进入职业大洗牌时代，“吃香”职业还香吗？',
        'url': 'https://new.qq.com/omn/20210828/20210828A025LKOO.html'
    },
    {
        'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
        'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    },
    {
        'title': '他，活出了我们理想的样子',
        'url': 'https://new.qq.com/omn/20210821/2021082821A020ID00.html'
    }
]

# client.indices.delete(index='msgs')

for data in datas:
    client.index(index='msgs', body=data)

result = client.search(index='msgs')
print(result)

dsl = {
    'query': {
        'match': {
            'title': '高考 圆梦'
        }
    }
}

result = client.search(index='msgs', body=dsl)
print(result)   # 查看得分值_score