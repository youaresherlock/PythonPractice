#!usr/bin/python
# -*- coding:utf8 -*-
import socket 


if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1', 9000))
    send_data = '你好服务端, 我是客户端小黑!'.encode('utf8')
    tcp_client_socket.send(send_data)
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data)
    recv_content = recv_data.decode('utf8')
    print('接受服务端的数据为:', recv_content)
    tcp_client_socket.close()

















