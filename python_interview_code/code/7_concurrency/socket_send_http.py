#!usr/bin/python
# -*- coding:utf8 -*-

# 使用socket发送http请求
import socket

s = socket.socket()
s.connect(('www.baidu.com', 80))

http = b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"
s.sendall(http)
result = ''
buf =s.recv(1024)
while buf:
    result += buf.decode()
    buf = s.recv(1024)
print(result)
s.close()