# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-03 21:56:19
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-03 22:39:19
"""
假设有一群生产者和一群消费者，他们通过一个市场来交换产品 生产者的策略:如果市场上的
剩余的产品少于1000个的时候，那么就生产100个产品投放到市场中;消费者的策略:如果市场上
剩余的产品数量多于100个的时候，那么就消费3个产品。
高并发编程中 对于解决线程同步问题的经典案例 生产者与消费者模型
条件变量去实现(队列也可以)


Condition的基本原理:
Condition对象维护了一个锁（Lock/RLock)和一个waiting池。
线程通过acquire获得Condition对象，当调用wait方法时，
线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程。
当调用notify方法时，Condition对象会从waiting池中挑选一个线程，
通知其调用acquire方法尝试取到锁
"""
import threading
import time


class Producer(threading.Thread):
    # 当使用继承的方式创建线程时，一定要重写父类的run方法
    def run(self):
        # 告诉我们的Python解释器，我要对全局变量进行修改了
        global count
        # 这个死循环就是用来模拟市场上的交易行为
        while True:
            # 判断生产者是否获得了锁
            if con.acquire():
                print(f'生产者: {self.name}抢到锁了')
                # 生产者的产品数量是否足够
                if count > 1000:
                    # 当生产者生产了足够多的产品时，便让生产者进入阻塞状态
                    con.wait()
                # 生产者生产100个产品
                else:
                    count += 100
                    msg = self.name + '生产者生产了100个产品，总数量=' + str(count)
                    print(msg)
                    # 生产者通知消费者
                    con.notify()
                con.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                print(f'消费者: {self.name}抢到锁了')
                if count < 100:
                    con.wait()
                else:
                    count -= 3
                    msg = self.name + '消费者消费了3个产品，剩余产品数量=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
            time.sleep(1)


if __name__ == '__main__':
    # 定义初始商品
    count = 500
    # 创建条件变量
    con = threading.Condition()
    # 创建三个生产者
    for i in range(3):
        producer = Producer()
        producer.start()
    # 创建5个消费者
    for i in range(5):
        consumer = Consumer()
        consumer.start()
