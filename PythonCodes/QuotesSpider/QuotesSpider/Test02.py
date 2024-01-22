# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/4 13:00
@Auth ： 异世の阿银
@File ：Test02.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


class MySpider:

    spider = "MySpider 123"

    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls):
        m = cls()  # cls 类名     实例化
        m.m_test()
        return m

    def m_test(self):
        print("m_test")

    def test(self):
        print("test")


class MySpider2:

    spider = "MySpider 234"     # 类属性

    @classmethod
    def from_crawler(cls, spider):  # spider = m3
        print('=' * 100)
        print(cls)
        print(spider)   # 要处理的spider是MySpider
        m = cls()
        m._set_spider(spider)
        print('=' * 100)
        return m

    def _set_spider(self, spider):
        print('^' * 100)
        print(self)
        print(spider)
        self.spider = spider
        print('^' * 100)

    def test(self):
        print('!' * 100)
        print(f'实例: {self}')
        print(f'实例变量: {self.spider}')
        print(f'类属性: {self.spider.spider}')
        print('!' * 100)


if __name__ == '__main__':
    # 1. 实例化  实例方法
    m1 = MySpider()
    m1.test()
    print('-' * 100)
    # 2. 实例化  类方法  classmethod
    m2 = MySpider.from_crawler()
    m2.test()
    print('-' * 100)
    # 传递spider类m3
    m3 = MySpider.from_crawler()
    r = MySpider2.from_crawler(m3)
    r.test()


    # 一个作为主类, 和一个不重要的类
