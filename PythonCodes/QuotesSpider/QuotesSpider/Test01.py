# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/4 9:55
@Auth ： 异世の阿银
@File ：Test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


class TestGetAttr:
    # name = "coffee"

    def test(self):
        name = getattr(self, 'name', 'buffer')      # 如果没有name则得到buffer
        print(name)
        name = hasattr(self, 'name')
        print(name)


if __name__ == '__main__':
    t = TestGetAttr()
    t.test()


