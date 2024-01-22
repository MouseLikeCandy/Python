# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/4 17:25
@Auth ： 异世の阿银
@File ：fingerprint.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


import hashlib
from w3lib.url import canonicalize_url
'''
Scrapy 中实现去重的原理

指纹不是加密 一般是哈希算法生成的  散列值
只能正着来 666 -> 627ea51d87746eaf2ef9603c81330f5c4159343b

正向开发: 一般作为密码的校验

# 运行爬虫, 将指纹保存下来
scrapy crawl quotes -s  JOBDIR=./seen

JOBDIR 断点续爬
'''


username = "张三"
password = '666'  # 明文    数据库中存储cd3f0c85b158c08a2b113464991810cf2cdfc387  存储到数据库做校验

result = hashlib.sha1(b'666').hexdigest()   # 16进制
print(result)
result = hashlib.sha1(b'666.').hexdigest()
print(result)
print("-" * 100)

start_urls = ["https://baidu.com?name=jack&age=9", "https://baidu.com?age=9&name=jack", "https://sougou.com"]

dfs = set()     # 集合


def request_seen(seen_url):
    # url_result = hashlib.sha1(seen_url.encode()).hexdigest()    # 对应fp = self.request_fingerprint(request)

    url_result = hashlib.sha1(canonicalize_url(seen_url.encode()).encode()).hexdigest()

    if url_result in dfs:       # url_result 即是 fp
        print("重复了 不再采集")
        return True
    else:
        print("不重复 进入队列")
        dfs.add(url_result)
        return False


for url in start_urls:
    request_seen(url)
    print(request_seen(url))

print(dfs)
