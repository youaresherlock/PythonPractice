#!usr/bin/python
# -*- coding:utf8 -*-
"""
SETNX lock1  1   # 键不存在,才会设置成功
$ 1
SETNX lock1  1   # 键存在, 无法设置, 返回0
$ 0
"""

from redis import StrictRedis

# 创建redis连接
redis_client = StrictRedis(decode_responses=True)

# 设计redis悲观锁 处理秒杀超卖问题

# 先获取锁
while True:
    order_lock = redis_client.setnx('lock:order', 1)
    if order_lock:
        # 防止死锁,5秒后锁没有释放自动过期释放
        redis_client.expire('lock:order', 5)  # 给锁设置过期时间, 超出5秒, 自动删除锁

        reserve_count = redis_client.get('count:reserve')
        if int(reserve_count) > 0:
            redis_client.decr('count:reserve')
            print("生成订单")
        else:
            print("已售罄")
        # 完成处理, 移除锁
        redis_client.delete('lock:order')
        break




















