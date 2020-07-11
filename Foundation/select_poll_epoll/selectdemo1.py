#!usr/bin/python
# -*- coding:utf8 -*-
"""
    网络通讯被unix系统抽象为文件的读写,通常是一个设备,由设备驱动程序提供,驱动可以知道自身的
数据是否可用. 设备的文件的资源如果可用(可读或者可写)则会通知进程,反之则会让进程睡眠,等到
数据到来可用的时候,再唤醒进程.
    这些设备的文件描述符被放在一个数组中,然后select调用的时候遍历这个数组,如果对于文件描述符
可读则会返回文件描述符.当遍历结束之后,如果仍然没有一个可用设备文件描述符,select让用户进程则会
睡眠，直到等待资源可用的时候在唤醒,遍历之前那个监视的数组.每次遍历都是线性的.
select回显服务器
"""
import select
import socket
import sys

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

inputs = [server, sys.stdin]
running = True

while True:
    try:
        # 调用 select 函数，阻塞等待
        readable, writeable, exceptional = select.select(inputs, [], [])
    except select.error as e:
        break

    # 数据抵达，循环
    for sock in readable:
        # 建立连接
        if sock == server:
            conn, addr = server.accept()
            # select 监听的socket
            inputs.append(conn)
        elif sock == sys.stdin:
            junk = sys.stdin.readlines()
            running = False
        else:
            try:
                # 读取客户端连接发送的数据
                data = sock.recv(BUFFER_SIZE)
                if data:
                    sock.send(data)
                    if data.endswith('\r\n\r\n'):
                        # 移除select监听的socket
                        inputs.remove(sock)
                        sock.close()
                else:
                    # 移除select监听的socket
                    inputs.remove(sock)
                    sock.close()
            except socket.error as e:
                inputs.remove(sock)

server.close()










































































