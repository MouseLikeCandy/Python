import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'Quotes'     # 爬虫名字
    allowed_domains = ['toscrape.com']      # 域名
    start_urls = ['https://quotes.toscrape.com/page/1/', 'https://quotes.toscrape.com/page/2/']
    # start_urls = ['https://quotes.toscrape.com/page/5/']
    # 网址列表,也可以是元组  能循环迭代就可以

    custom_settings = {     # 重写配置文件, 自定义配置文件(个性化配置), 会覆盖setting.py中的内容 setting.py是公共的配置文件
        # 如果两个爬虫用的配置文件不一样就很有用了
        "DEFAULT_REQUEST_HEADERS": {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            # yield scrapy.Request(url, dont_filter=True)     # 不对请求列表start_urls中的网址去重False去重  get请求（默认）
            yield scrapy.Request(url, dont_filter=False)
            # yield scrapy.FormRequest(url, dont_filter=True)     # Post请求

    def parse(self, response):
        # 1. 选择出数据
        for quote in response.css('div.quote'):     # css  网址上右键检查找到html标签位置

            yield {
                'author': quote.xpath('span/small/text()').get(),   # xpath
                'text': quote.css('span.text::text').get(),         # css
            }
        # # 2. 翻页
        # next_page = response.css('li.next a::attr("href")').get()   # /page/4/
        # if next_page is not None:
        #     # yield scrapy.Request(next_page, callback=self.parse)   # 之前使用, callback不写也可以, 然后拼接网址
        #     self.log(f"这是我的信息---打印当前翻页{next_page}")
        #     # 拼接 'https://quotes.toscrape.com' + '/page/4/'
        #     yield response.follow(next_page, self.parse)    # 新的知识点follow, 里面有urljoin()

    def closed(self, reason):
        self.log("我是关闭爬虫后执行的函数 closed")
        self.log("你可以在此处发送一个邮件 closed")
        self.log(f"这是关闭爬虫的原因:{reason}")

'''
    修改settings.py 配置文件
    1. 修改robot协议 为False
    2. 加上请求头 DEFAULT_REQUEST_HEADERS 从浏览器中找到请求头
    
    数据保存
    方式一: 在管道中保存数据 在设置文件settings.py中激活管道文件
    方式二: scrapy crawl quotes  -o quotes.csv                # -o 直接保存为表格数据
'''

'''
使用以下指令得到指纹的文件
scrapy crawl Quotes -s  JOBDIR=./seen

现象:
当 start_urls 中只有一个请求地址时, 然后也不使用follow或拼接url, 即只有一个请求, requests.seen没有得到指纹
当 start_urls 中只有一个请求地址时, 使用follow或拼接url时, 本案例共有10个请求, requests.seen得到9个指纹
当 start_urls 中只有多个请求地址时, 然后也不使用follow或拼接url, requests.seen没有得到指纹

个人结论: 不会为 start_urls 列表中的请求添加指纹, 而会对自动找到的请求添加指纹(错误的)

真实情况:
Scrapy 提供了一个很好的请求指纹过滤器(Request Fingerprint duplicates filter)
scrapy.dupefilters.ReppupeFilter ,当它被启用后,会自动记录所有成功返回响应的请求的URL，并将其以文件
(requests.seen)方式保存在项目目录中。请求指纹过滤器的原理是为每个URL生成一个指纹并记录下来,一旦
当前请求的URL在指纹库中有记录,就自动跳过该请求。
默认情况下这个过滤器是自动启用的，但是在 start_requests 中是关闭的,当然也可以根据自身的需求编写自定义的过滤器。

yield scrapy.Request(url, dont_filter=True)  True: 不对请求列表 start_urls 中的网址去重  False: 去重
'''

'''
博客的重要性 -- 输出思想

服务器搭建
阿里云 / 腾讯云 / 亿云
Linux 80% - 90%能够用到, 小公司可能都是一个人的活

用火狐驱动, 代替谷歌, 应用: 瑞数, 淘宝滑块

多线程编程:
thread 麻烦一些
concurrent.futures 高并发
<安卓Fida逆向与开发实战>
'''