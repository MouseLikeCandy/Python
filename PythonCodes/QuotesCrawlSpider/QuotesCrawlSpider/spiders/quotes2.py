import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'Quotes'     # 爬虫名字
    allowed_domains = ['toscrape.com']      # 域名
    start_urls = ['https://quotes.toscrape.com/page/1/', 'https://quotes.toscrape.com/page/1/']   # 网址  能循环迭代就可以

    custom_settings = {     # 重写配置文件
        "DEFAULT_REQUEST_HEADERS": {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True)     # 对请求列表start_urls中的网址去重   get请求（默认）
            yield scrapy.FormRequest(url, dont_filter=True)     # Post请求

    def parse(self, response):
        # 1. 选择出数据
        for quote in response.css('div.quote'):     # css  网址上右键检查找到html标签位置

            yield {
                'author': quote.xpath('span/small/text()').get(),   # xpath
                'text': quote.css('span.text::text').get(),         # css
            }
        # 2. 翻页
        next_page = response.css('li.next a::attr("href")').get()   # /page/4/
        if next_page is not None:
            self.log(f"这是我的信息---打印当前翻页{next_page}")
            # 拼接 'https://quotes.toscrape.com' + '/page/4/'
            yield response.follow(next_page, self.parse)    # 知识点follow

    def closed(self, reason):
        self.log("我是关闭爬虫后执行的函数 closed")
        self.log("你可以在此处发送一个邮件 closed")
        self.log(f"这是关闭爬虫的原因:{reason}")
