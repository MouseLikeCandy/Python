import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QuotesSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/4']

    # 链接提取器
    link_extractor = LinkExtractor(allow=r'http://quotes.toscrape.com/page/\d+/')        # 链接提取器, 提取网址的    allow=r'Items/' 允许提取哪些  正则
    # link_extractor = LinkExtractor(allow=r'/page/\d+/')
    # 一系列规则, 重点
    rules = (
        Rule(link_extractor=link_extractor, callback='parse_item', follow=False),    # follow=True 继续追踪 True才是全站
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        for quote in response.css('div.quote'):
            yield{
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        return item
