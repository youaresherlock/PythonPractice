#!usr/bin/python
# -*- coding:utf8 -*-

# 编写一个兼容WSGI的小应用
def myapp(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]

    start_response(status, headers)
    print(environ)
    # 返回可迭代的字节对象
    return [b'<h1>Hello World</h1>'] # 可迭代对象，返回字节

# web app有了，还差一个web server 
if __name__ == '__main__':
    from wsgiref.simple_server import make_server 
    httpd = make_server('127.0.0.1', 8888, myapp)
    httpd.serve_forever()