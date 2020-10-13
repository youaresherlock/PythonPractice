#!usr/bin/python
# -*- coding:utf8 -*-
"""
redis的事务和管道可以分离, 可以 不使用事务的情况下单独使用管道
管道可以实现 一次发送多条命令给redis服务器, 提高传输效率
"""

from redis import StrictRedis

# 创建redis客户端
redis_client = StrictRedis()

# 创建管道对象  设置transaction参数为False, 则会创建非事务型管道(只开管道, 不开事务)
pipe = redis_client.pipeline(transaction=False)

# pipe的后续操作会被管道中
a = pipe.set('name', 'zhangsan')
b = pipe.get('name')

# 执行管道  会让管道将命令打包发给redis服务器
c = pipe.execute()

print(a)
print(b)
print(c)