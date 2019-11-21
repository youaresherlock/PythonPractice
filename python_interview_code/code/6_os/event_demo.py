#!usr/bin/python
# -*- coding:utf8 -*-
'''
Event是最简单的线程间通信机制，一个线程负责给事件发信号，其他线程等待事件。
Event类内部有一个flag标识，初始值为False。
Event类常用的三个方法有：set、clear、wait。set方法会将flag标识置为True，
所有处于等待的线程将会被唤醒；clear方法会将flag重置为False；wait方法将阻塞线程，除非flag标识被置为True。
'''

import threading
import time

ev=threading.Event()

def func():
    print('%s waits event...' % threading.currentThread().getName())
    ev.wait()
    print('%s receives event...' % threading.currentThread().getName())



if __name__ == '__main__':
    t1=threading.Thread(target=func,args=())
    t2=threading.Thread(target=func,args=())

    t1.start()
    t2.start()

    time.sleep(5) #主线程休眠5秒

    print('main thread sets event...')
    ev.set() #主线程设置事件e
