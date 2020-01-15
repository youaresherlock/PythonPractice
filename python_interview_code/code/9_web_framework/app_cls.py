#!usr/bin/python
# -*- coding:utf8 -*-

class Application(object):

    def __init__(self, routers, **kwargs):
        self.routers = routers 

    # 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
    def __call__(self, environ, start_response):
        try:
            request = Request(environ)
            callback, args = routers.match(request.path)
            response = callback(request, *args)
        except NotFoundError:
            response = Response("<h1>Not found</h1>", status=404)
        start_response(response.status, response.headers.items())
        return iter(response)