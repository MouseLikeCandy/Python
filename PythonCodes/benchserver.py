# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/5 18:07
@Auth ： 异世の阿银
@File ：benchserver.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
复制一个benchserver   http://localhost:8998/
path = r'D:\\Python3.7.3\\Lib\\site-packages\\scrapy\\utils\\benchserver.py'

twisted 可以研究
'''
import random
from urllib.parse import urlencode

from twisted.web.server import Site
from twisted.web.resource import Resource


class Root(Resource):

    isLeaf = True

    # def getChild(self, name, request):
    #     return self

    def render(self, request):
        # total = _getarg(request, b'total', 100, int)
        # show = _getarg(request, b'show', 10, int)
        # nlist = [random.randint(1, total) for _ in range(show)]
        # request.write(b"<html><head></head><body>")     # 头
        # args = request.args.copy()
        # for nl in nlist:
        #     args['n'] = nl
        #     argstr = urlencode(args, doseq=True)
        #     request.write(f"<a href='/follow?{argstr}'>follow {nl}</a><br>"
        #                   .encode('utf8'))
        # request.write(b"</body></html>")
        return b'hello world!'


# def _getarg(request, name, default=None, type=str):
#     return type(request.args[name][0]) if name in request.args else default


if __name__ == '__main__':
    from twisted.internet import reactor
    root = Root()   # 资源实例化
    factory = Site(root)
    # httpPort = reactor.listenTCP(8998, Site(root))
    httpPort = reactor.listenTCP(8998, factory)

    def _print_listening():
        httpHost = httpPort.getHost()
        print(f"Bench server at http://{httpHost.host}:{httpHost.port}")
    reactor.callWhenRunning(_print_listening)
    reactor.run()
