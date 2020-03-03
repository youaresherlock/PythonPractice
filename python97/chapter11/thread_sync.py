#!usr/bin/python
# -*- coding:utf8 -*-
# gil global interpreter lock (ipython)
# python中一个线程对应c语言中的一个线程
# gil使得同一时刻只有一个线程运行在一个CPU上执行字节码，无法将多个线程映射到多个cpu上
# gil会根据执行的字节码行数以及时间片释放GIL，遇到IO操作也会释放
# import dis
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))

from threading import Lock

total = 0
lock = Lock()
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()
import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)


# 1.用锁会影响性能
# 2. 锁会影响性能 四个必要条件

























