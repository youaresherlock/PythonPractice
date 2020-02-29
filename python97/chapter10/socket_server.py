#!usr/bin/python
# -*- coding:utf8 -*-
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

"""
import threading 
def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024) 
        print(data.decode("utf8")
        re_data = input() 
        sock.send(re_data.encode("utf8")
        
while True:
    sock, addr = server.accept() 
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr) 
    client_thread.start() 
    
"""

sock, addr = server.accept()

# 获取从客户端发送的数据
# 一次获取1KB数据
data = sock.recv(1024)
print(data.decode('utf8'))
sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))
server.close()
sock.close()



























