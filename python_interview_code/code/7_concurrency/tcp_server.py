#!usr/bin/python
# -*- coding:utf8 -*-

import time
import socket

s = socket.socket()
s.bind(('', 8888))
s.listen()

while True:
    client, addr = s.accept() # return conn, addr
    print(client, addr)
    timestr = time.ctime(time.time()) + '\r\n'
    client.send(timestr.encode()) # send参数encode('utf8')
    data = client.recv(1024)
    print(data.decode())
    client.close()
