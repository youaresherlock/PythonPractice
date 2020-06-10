# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-06-10 18:40:18
# @Last Modified by:   Clarence
# @Last Modified time: 2020-06-10 18:47:37
from my_middleware import router 

#here is the application

@router('/hello')	#调用 route 实例，把函数注册到 paht_info 字典

def hello(environ, start_response):

    status = '200 OK'

    output = 'Hello'

    response_headers = [('Content-type', 'text/plain'),

                        ('Content-Length', str(len(output)))]

    write = start_response(status, response_headers)

    return [output]

 

@router('/world')

def world(environ, start_response):

    status = '200 OK'

    output = 'World!'

    response_headers = [('Content-type', 'text/plain'),

                        ('Content-Length', str(len(output)))]

    write = start_response(status, response_headers)

    return [output]

 

#here run the application

result = router.route(environ, start_response)

for value in result:

    write(value)