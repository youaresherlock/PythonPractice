#!usr/bin/python
# -*- coding:utf8 -*-

"""
信号量主要用在保护有限的资源。
以数据库连接数为例说明，假设当前数据库支持最大连接数为3, 将信号量初始值设为3，那么同时最大
可能有三个线程连接数据库，其他线程若再想连接数据库，则只有等待，直到某一个线程释放数据库连接

主线程默认是not daemon, 因此子线程默认是非守护线程. 主线程执行完自己任务以后，就退出了，
此时子线程会继续执行自己的任务，直到自己的任务结束.
当设置子线程为守护线程时,主线程一旦结束，则全部线程全部被终止执行

join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待
其他的子线程执行结束之后，主线程在终止
"""
import time
import threading

sm = threading.Semaphore(3)

def connectDb():
    test = sm.acquire()

    print(threading.currentThread().getName() + ' connecting to db...\n', test)
    time.sleep(2)
    print(threading.currentThread().getName() + ' released db...\n')

    sm.release()

def main():
    threads = []
    for i in range(20):
        t = threading.Thread(target=connectDb)
        threads.append(t)
    for t in threads:
        # t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print(end - start)







