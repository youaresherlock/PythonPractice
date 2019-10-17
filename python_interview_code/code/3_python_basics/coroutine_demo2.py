#!usr/bin/python
# -*- coding:utf8 -*-

'''
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁
机制控制队列和等待，但一不小心就可能思索.
如果改用协程，生产者生产消息后，直接通过yeild跳转到消费者开始执行, 待消费者执行
完毕后，切换回生产者继续生产，效率极高
'''

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming {}...'.format(n))
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 10:
        n = n + 1
        print('[PRODUCER] Producing {}...'.format(n))
        r = c.send(n)
        print('[PRODUCER] Consumer return: {}'.format(r))

    c.close()

c = consumer()
produce(c)

'''
consumer函数是一个generator,把一个consumer传入produce后:
1. 首先调用c.send(None)启动生成器
2. 然后，一旦生成了东西,通过c.send(n)切换到consumer执行
3. consumer通过yield拿到消息，处理,又通过yield把结果传回
4. produce拿到consumer处理的结果，继续生产下一条消息
5. produce决定不生产了,通过c.close()关闭consumer,整个过程结束
整个流程无锁，由一个线程执行,produce和consumer协作完成任务，所以称为"协程", 而非线程的抢占式多任务
'''



























