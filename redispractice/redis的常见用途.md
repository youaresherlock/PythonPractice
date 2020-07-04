redis是键值对的数据库,常用的五种数据类型为字符串类型(string),散列类型(hash),列表类型(list),
集合类型(set), 有序集合类型(zset)

Redis用作缓存,主要两个途径: 高性能,高并发, 因为内存天然支持高并发

1. 分布式锁(string)：
setnx key value， 当key不存在时,将key的值设为value,返回1. 若给定的key已经存在,
则setnx不做任何动作,返回0 

当setnx返回1时,表示获取锁, 做完操作以后del key,表示释放锁,如果setnx返回0表示获取锁失败, 
整体思路大概就是这样 

2. 计数器(string)
如知乎每个问题的被浏览器次数 
set key 0
incr key // incr readcount::{帖子id} 每阅读一次
get key // get readcount::{帖子id} 获取阅读量

3. 消息队列(list)
一直往list左边放
lpush key value 
key这个list有元素时，直接弹出，没有元素被阻塞，直到等待超时或发现可弹出元素为止，上面例子超时时间为10s
brpop key value 10 

4. 排行榜(zset) 
redis的zset天生是用来做排行榜的、好友列表、去重、历史记录等业务需求

ZREVRANGE key start stop [WITHSCORES]
返回有序集 key 中，指定区间内的成员。
*user1的用户分数为 10*
zadd ranking 10 user1
zadd ranking 20 user2

# 取分数最高的3个用户
zrevrange ranking 0 2 withscores























