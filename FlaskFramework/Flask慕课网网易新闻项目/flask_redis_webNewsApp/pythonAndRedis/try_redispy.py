#!usr/bin/python
# -*- coding: utf8 -*-
import redis

class Base(object):
    def __init__(self):
        # 连接池默认最大连接max_connections 2 ** 31
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.r = redis.Redis(connection_pool=self.pool)

class TestString(Base):
    def test_set(self):
        ''' 使用set设置值 '''
        rest = self.r.set('user2', 'Amy')
        print(rest)

    def test_get(self):
        ''' 使用get获取值 '''
        rest = self.r.get('user2')
        print(rest)

    def test_mset(self):
        ''' mset设置多个键值对 '''
        d = {
            'user3': 'Bob',
            'user4': 'Box'
        }
        rest = self.r.mset(d)
        print(rest)

    def test_mget(self):
        ''' mget获取多个键值对 '''
        l = ['user3', 'user4']
        rest = self.r.mget(l)
        print(rest)
        return rest

    def test_del(self):
        ''' del string '''
        rest = self.r.delete('user3')
        print(rest)

class TestList(Base):
    def test_push(self):
        ''' lpush/rpush 从左/右插入数据 '''
        t = {'Amy', 'John'}
        rest = self.r.lpush('l_eat', *t)
        print(rest)
        rest = self.r.lrange('l_eat', 0, -1)
        print(rest)

    def test_pop(self):
        ''' lpop/rpop移除最左/右的元素并返回 '''
        rest = self.r.lpop('l_eat')
        print(rest)
        rest = self.r.lrange('l_eat', 0, -1)
        print(rest)

class TestSet(Base):
    """
    sadd/srem -- 添加/删除元素
    sismember -- 判断是否为set的一个元素
    smembers -- 返回该集合的所有成员
    sdiff -- 返回一个集合与其它集合的差异
    sinter -- 返回几个集合的交集
    sunion -- 返回几个集合的并集
    """
    def test_sadd(self):
        l = ['Horse', 'Tiger', 'Wolf', 'Monkey', 'Sheep', 'Rabbit', 'Mouse']
        rest = self.r.sadd('zoo3', *l)
        print(rest)
        rest = self.r.smembers('zoo3')
        print(rest)

    def test_srem(self):
        rest = self.r.srem('zoo2', 'Dog')
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_sinter(self):
        rest = self.r.sinter('zoo2', 'zoo3')
        print(rest)

class TestHash(Base):
    """
    hset/hget -- 设置/获取散列值
    hmset/hmget -- 设置/获取多对散列值
    hsetnx -- 如果散列已经存在，则不设置
    hkeys/hvals -- 返回所有Keys/Values
    hlen -- 返回散列包含域(field)的数量
    hdel -- 删除散列指定的域(field)
    hexists -- 判断是否存在
    """
    def test_set(self):
        rest = self.r.hset('stu:xxx02', 'name', 'John')
        print(rest)
        rest = self.r.hget('stu:xxx02', 'name')
        print(rest)

    def test_hmset(self):
        m = {'name': 'Bob', 'age': 21, 'grade': 90}
        rest = self.r.hmset('stu:xxx03', m)
        print(rest)
        rest = self.r.hkeys('stu:xxx03')
        print(rest)


def main():
    # obj = TestString()
    # obj.test_set()
    # obj.test_get()
    # obj.test_mset()
    # obj.test_mget()
    # obj.test_del()

    # list_obj = TestList()
    # list_obj.test_push()
    # list_obj.test_pop()

    # set_obj = TestSet()
    # set_obj.test_sadd()
    # set_obj.test_srem()
    # set_obj.test_sinter()

    hash_obj = TestHash()
    # hash_obj.test_set()
    hash_obj.test_hmset()
if __name__ == '__main__':
    main()