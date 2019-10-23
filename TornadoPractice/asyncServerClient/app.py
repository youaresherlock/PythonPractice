#!usr/bin/python
# # -*- coding:utf8 -*-

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("base.html")

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("500.html", msg="We're sorry, but something went wrong.")

def make_app():
    return tornado.web.Application(
        [
        (r"/", MainHandler),
        (r"/500", ErrorHandler)
        ],
        template_path=os.path.join(
            os.path.dirname(__file__), "templates"
        ),
        debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

