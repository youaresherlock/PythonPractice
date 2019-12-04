#!usr/bin/python
# -*- coding:utf8 -*-

import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class APIHandler(tornado.web.RequestHandler):
    async def get(self):
        url = 'http://httpbin.org/get'
        http_client = AsyncHTTPClient()
        resp = await http_client.fetch(url)
        print(resp.body)
        return resp.body

def make_app():
    return tornado.web.Application([
        (r'/api', APIHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()