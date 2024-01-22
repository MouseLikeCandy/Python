# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/14 20:59
@Auth ： 异世の阿银
@File ：item_pipelines.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
参考案例: https://docs.scrapy.org/en/latest/topics/item-pipeline.html Take screenshot of item 可以理解为截一张图
'''
import hashlib
from pathlib import Path
from urllib.parse import quote

import scrapy
from itemadapter import ItemAdapter
from scrapy.http.request import NO_CALLBACK
from scrapy.utils.defer import maybe_deferred_to_future


class ScreenshotPipeline:
    """Pipeline that uses Splash to render screenshot of
    every Scrapy item."""

    SPLASH_URL = "http://localhost:8050/render.png?url={}"

    async def process_item(self, item, spider):     # async 异步写法, 部门代码, 协程函数, await
        adapter = ItemAdapter(item)
        encoded_item_url = quote(adapter["url"])
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screenshot_url, callback=NO_CALLBACK)
        response = await maybe_deferred_to_future(
            spider.crawler.engine.download(request, spider)     # 核心代码, 延迟对象
        )

        if response.status != 200:
            # Error happened, return item.
            return item

        # Save screenshot to file, filename will be hash of url.
        url = adapter["url"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        filename = f"{url_hash}.png"
        Path(filename).write_bytes(response.body)

        # Store filename in item.
        adapter["screenshot_filename"] = filename
        return item
