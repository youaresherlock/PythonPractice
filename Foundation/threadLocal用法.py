#!usr/bin/python
# -*- coding:utf8 -*-
import time
import threading


instance = threading.local()


def worker(number):
    instance.number = number
    print(threading.current_thread(), instance.number)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=worker, args=(i,)).start()
