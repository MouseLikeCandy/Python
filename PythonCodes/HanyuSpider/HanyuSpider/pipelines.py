# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import hashlib
import scrapy
from scrapy.utils.defer import maybe_deferred_to_future     # 可能是延迟的
from scrapy.pipelines.images import ImagesPipeline

from twisted.internet import threads    # 导入线程池
#
#
# class HanyuspiderPipeline:
#     def process_item(self, item, spider):
#
#         print(f"process_item: {item}")
#
#         gif = item.get('gif')
#         if gif:
#             response = requests.get(gif)
#             self.save_image(response)
#
#         return item
#
#     def save_image(self, resposne: requests.Response):
#         name = hashlib.md5(resposne.content).hexdigest()   # 十六进制
#         with open('../images/' + name + 'gif', 'wb') as fp:
#             fp.write(resposne.content)

'''
弊端: 既要用scrapy, 又用了requests

只用scrapy如何做? 
参考案例: https://docs.scrapy.org/en/latest/topics/item-pipeline.html Take screenshot of item 可以理解为截一张图
'''


# class HanyuspiderPipeline:
#     async def process_item(self, item, spider):
#         gif = item.get('gif')
#         if gif:
#             request = scrapy.Request(gif)
#             response = await maybe_deferred_to_future(
#                 spider.crawler.engine.download(request, spider)  # 核心代码, 延迟对象
#             )
#             # response = await spider.crawler.engine.download(request, spider)
#             self.save_image(response.body)
#         return item
#
#     def save_image(self, content):     # 响应是scrapy里面的响应
#         name = hashlib.md5(content).hexdigest()
#         with open('../images/' + name + 'gif', 'wb') as fp:
#             fp.write(content)


'''
多线程版本: 采集快, 保存慢
Andy老师: 麦艳涛  http://maiyantao.com/

推荐使用
'''
# class HanyuspiderPipeline:
#     def process_item(self, item, spider):
#         gif = item.get('gif')
#         if gif:
#             d = threads.deferToThread(self.get_gif, gif)             # 用线程池的方式 10线程, 返回值是回调对象
#             d.addCallbacks(self.on_success, self.on_error)           # 添加回调函数
#             return d
#
#     def get_gif(self, gif):
#         response = requests.get(gif)
#         return response.content
#
#     def on_success(self, content):
#         name = hashlib.md5(content).hexdigest()
#         with open('../images/' + name + 'gif', 'wb') as fp:
#             fp.write(content)
#
#     def on_error(self, result):
#         print("保存图片回调失败!")

'''
scrapy 源码 pipelins - images.py scrapy默认有保存图片, 但不保存gif
ImagesPipeline 类
get_iamges()
image_downloaded()
get_media_requests() 重写这个请求
file_path()

在 setting 中配置路径 IMAGE_STORE
'''
class HanyuspiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # urls = ItemAdapter(item).get(self.images_urls_field, [])
        # return [Request(u) for u in urls]
        url = item.get("gif", "")
        yield scrapy.Request(url)    # 只有一个网址

    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        return imgName

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类

