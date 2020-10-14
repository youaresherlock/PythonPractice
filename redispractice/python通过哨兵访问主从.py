#!usr/bin/python
# -*- coding:utf8 -*-
from redis.sentinel import Sentinel

sentinels = [  # 设置哨兵的IP和端口
    ('192.168.105.140', 26380),
    ('192.168.105.140', 26381),
    ('192.168.105.140', 26382),
]

# 创建哨兵客户端
sentinel_client = Sentinel(sentinels)

# 主数据库别名
service_name = 'mymaster'

# 获取主数据库
redis_master = sentinel_client.master_for(service_name, decode_responses=True)
# 获取从数据库
redis_slave = sentinel_client.slave_for(service_name, decode_responses=True)

# print(type(redis_master))

redis_master.zadd('movies', 8, 'dahuaxiyou')
redis_master.zincrby('movies', 'dahuaxiyou', 2)
print(redis_master.zscore('movies', 'dahuaxiyou'))

# 主数据库进行数据操作
# redis_master.set('name', 'zhangsan123')
# print(redis_master.get('name'))

# 从数据库进行数据操作
# print(redis_slave.get('name'))
# redis_slave.set('name', 'lisi')  # 不能写

# 写操作, 直接使用主
# 读操作, 直接使用从
# 有读有写, 建议使用主   可以使用 管道 / 乐观锁



























