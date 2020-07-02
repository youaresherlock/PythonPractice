#!usr/bin/python
# -*- coding:utf8 -*-
"""
python协程实现生产者和消费者模型
generator.send(value):
    Resumes the execution and "sends" a value into the generator function. The value
argument becomes the result of the current yield expression. The send() method returns
the next value yields by the generator, or raises StopIteration if the generator exits
without yielding another value .
"""


def consumer():
    r = 'test'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # c.send(None)
    print(next(c))
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)









































