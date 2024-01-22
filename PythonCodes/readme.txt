# 创建一个Scrapy项目
	1. 创建项目 scrapy startproject xxxSpider   (xxx域名)     scrapy startproject QuotesSpider
	2. 创建爬虫 scrapy genspider Quotes toscrape.com  
	3. 编写项目 继承scrapy.Spider
	4. 运行爬虫 scrapy crawl quotes     # scrapy crawl quotes  -o quotes.csv   # -o直接保存表格数据



#Scrapy源码解读之scrapySpider
1.scrapy.Spider 是所有爬虫的基类 父类
2.name 需要重写名字唯一
3。custom_settings 重写配置文件 个性化配置文件
4.getattr获取实例的属性值
5.hasattr判断实例的属性值是否存在
6.start_urls 如果不写这个值 会设置为[]
7.self.log 是默认的日志 不用使用 print 了
8.dont_filter=Truq 请求中的一个参数 该参数设置为True的时候不会过滤请求 不对请求去重9.start_requests 是爬虫文件启动的关键 开始发起请求
10.raiseNotImplementedError 该异常会触发 提醒用户 需要重写 def parse 方法 并且一定要重写
11.callable判断一个对象是否可以调用
12.def closed(self，reason):一般是我们在关闭爬出的时候要做的事情 例如发个邮件