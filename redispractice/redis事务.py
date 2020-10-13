#!usr/bin/python
# -*- coding:utf8 -*-
"""
multi 开启事务,后续的命令被加入到同一个事务队列中, 服务端返回QUEUED
exec 执行exec后,事务中的命令才会被执行 当事务中的命令出现错误时,不会
回滚也不会停止事务,而是继续执行
discard 取消事务 事务队列会清空,客户端退出事务状态
"""
from redis import StrictRedis


# 创建redis客户端
redis_client = StrictRedis(decode_responses=True)

# 创建管道对象 默认会开启事务
pipe = redis_client.pipeline()

# pipe的后续操作会被放入事务中,不会立即执行
a = pipe.set('name', 'clarence')
b = pipe.get('name')

# 提交事务 提交才会执行事务中的命令
c = pipe.execute()

print(a)
print(b)
print(c)