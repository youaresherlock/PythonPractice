redis数据库基础

1. Redis数据库介绍
2. 安装及配置
3. Redis常用操作
4. 图形化管理工具操作Redis Desktop Manager


1. Redis数据库介绍
官方中文: http://www.redis.cn/
官方英文: https://redis.io/
中文教程: https://www.yiibai.com/redis/
https://www.yiibai.com/redis/redis_commands.html
用途:
数据库、缓存和消息中间件
类型:
字符串(strings)、散列(hashes)、列表(lists)、集合(sets)、有序集合(sorted sets)


2. 安装和配置
windows download: https://github.com/MicrosoftArchive/redis/releases
生产环境建议使用Linux stable版本

安装完毕可以设置配置文件 redis.windows-service.conf 默认为监听端口 6379
默认启动redis服务,进程列表有个redis-server.exe进程

连接本地redis服务器cmd->redis-cli


3. Redis常用操作
中文教程: https://www.yiibai.com/redis/
字符串(String)、列表(List)相关操作,集合(Set)相关操作、散列(Hash)相关操作

散列(hash)操作
hset/hget --- 设置/获取散列值
hmset/hmget --- 设置/获取多对散列值
hsetnx --- 如果散列已经存在，则不设置
hkeys/hvals --- 返回所有Keys/Values
hlen --- 返回散列包含域(field)的数量
hdel --- 删除散列指定的域(field)
hexists --- 判断是否存在

eg:
127.0.0.1:6379> hset news:3 title "Title3"
(integer) 0
127.0.0.1:6379> hget news:3 title
"Title3"
127.0.0.1:6379> hmset news:3 title "Title3" content "Content3" is_valid 1
OK
127.0.0.1:6379> hmget news:3 title content is_valid
1) "Title3"
2) "Content3"
3) "1"
127.0.0.1:6379> hlen news:3
(integer) 7
127.0.0.1:6379> hexists news:3 is_valid
(integer) 1
127.0.0.1:6379> del news:3 is_valid
(integer) 1


Python操作Redis
官方推荐库: redis-py
github: https://github.com/andymccurdy/redis-py
doc:  https://redis-py.readthedocs.io/en/latest/
1. redis-py安装及连接
2. 字符串(String)、列表(List)、集合(Set)、散列(Hash)操作

To install redis-py, simply:
$ pip install redis
or from source:
$ python setup.py install
















