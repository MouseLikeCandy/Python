import scrapy
from scrapy.http.response.text import TextResponse
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors import IGNORED_EXTENSIONS

'''
1. 创建项目 scrapy startproject HanyuSpider
2. 创建爬虫 scrapy genspider -l 列出模板爬虫 scrapy genspider (-t basic) hanyu baidu.com     需要进入项目
3. 编写爬虫 其实就是业务逻辑, 爬虫文件
4. 运行爬虫 scrapy crawl hanyu
'''


class HanyuSpider(scrapy.Spider):
    name = 'hanyu'
    # allowed_domains = ['baidu.com']
    start_urls = ['https://hanyu.baidu.com/s?wd=%E5%BF%83&ptype=zici']
    # https://hanyu-word-gif.cdn.bcebos.com/b81f9f9d0367f4bca8f4ea1872522b9ec.gif 笔顺的GIF图片

    # 自定义配置文件
    # custom_settings = {
    #     "ITEM_PIPELINES": {'HanyuSpider.pipelines.HanyuspiderPipeline': 300, }
    # }

    # def parse(self, response):
    def parse(self, response: TextResponse):
        # response.css().re()     # 指定具体类型之后, 后面可以有补全提示
        # self.log(response.text)
        # self.log(response.json())   # 是json()不是json

        # 1. 实现 相关字 & 热搜字 链接的提取
        link_extractor = LinkExtractor(restrict_css=".recmd-list")
        links = link_extractor.extract_links(response)
        for link in links:
            self.log(link.url)
            # response.follow_all(link)
            yield response.follow(link.url)

        # 2. 实现 gif 图片链接的提取 img 下的 src
        # link_extractor = LinkExtractor(restrict_css="#header-img")
        # link_extractor = LinkExtractor(restrict_css="#header-img", tags=('a', 'area', 'img'), attrs=('href', 'src'))
        # link_extractor = LinkExtractor(restrict_css=".alter-text", tags=('a', 'area', 'img'), attrs=('href', 'src'))
        link_extractor = LinkExtractor(restrict_css=".alter-text",
                                       tags=('a', 'area', 'img'),
                                       attrs=('href', 'data-gif'),
                                       deny_extensions=[])
        # 自己修改链接提取器参数 IGNORED_EXTENSIONS deny_extensions=['ckk', 'opp'] + IGNORED_EXTENSIONS.remove('apk')
        links = link_extractor.extract_links(response)
        if links:
            self.log("此处提取 gif: {}".format(links[0].url))  # 提取失败
            items = {
                "gif": links[0].url
            }
            yield items
        # 链接提取器默认只能提取 a area 标签
        # 通过 deny_extensions 定位到scrapy - linkextractors - __init__.py - IGNORED_EXTENSIONS 过滤的后缀
        # 删除源码中的 'gif'仍不好用



if __name__ == '__main__':
    cp = CrawlerProcess(settings=None)  # 可以把配置文件在这里指定  setting传入crawler.py
    cp.crawl(HanyuSpider)
    cp.start()

    '''
    记住运行scrapy的新的方法
    cp = CrawlerProcess()
    cp.crawl(HanyuSpider)
    cp.start()
    配置文件 & 管道文件, 以当前方法运行不加载管道和配置文件, 使用scrapy crawl hanyu 来运行则能够加载Robot协议
    '''

    '''
    提取数据
    使用调试 scrapy shell url
    
    view(response)  # 测试 scrapy 所看到的的和我们所看到的是否一致
    response.text   # 响应数据
    cls             # 清屏
    from scrapy.linkextractors import LinkExtractor  # 导包使用链接提取器
    link_extractor = LinkExtractor(restrict_css=".recmd-list")
    link_extractor.extract_links(response)

    
    怎么下载图片呢?
    https://hanyu-word-gif.cdn.bcebos.com/b6942dfa167cd4da79cc770009c064734.gif    
    '''

