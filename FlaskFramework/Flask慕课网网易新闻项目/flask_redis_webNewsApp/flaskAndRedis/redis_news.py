#!usr/bin/python
# -*- coding:utf8 -*-
import redis
import math

NEWS_FIELDS = (
    'title', 'img_url', 'content', 'is_valid', 'created_at', 'updated_at', 'news_type'
)

class Paginate(object):
    ''' 分页 '''
    def __init__(self, data_list, now_page, per_page):
        self.r = RedisNews()
        self.data_num = self.r.get_news_number()
        self.data_list = data_list
        self.now_page = now_page
        self.per_page = per_page

    @property
    def page(self):
        return self.now_page

    @property
    def items(self):
        ''' 当页数据 '''
        return self.data_list

    @property
    def has_prev(self):
        ''' 是否有上一页 '''
        return self.now_page > 1

    @property
    def has_next(self):
        ''' 是否有下一页 '''
        if len(self.data_list) < self.per_page:
            return False
        else:
            return  self.data_num > self.now_page * self.per_page

    @property
    def prev_num(self):
        ''' 上一页页码 '''
        return self.now_page - 1

    @property
    def next_num(self):
        ''' 下一页页码 '''
        return self.now_page + 1

    def iter_pages(self):
        ''' 页码 '''
        return range(1, int(math.ceil(self.data_num / self.per_page) + 1))


class RedisNews(object):
    def __init__(self):
        # 连接池默认最大连接max_connections 2 ** 31
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
        self.r = redis.Redis(connection_pool=self.pool)

    def __news_id(self, id):
        ''' 拼接新闻id  Key'''
        return 'news:%d' % int(id)

    def __news_type(self, cat):
        ''' 拼接新闻类表Key  '''
        return 'news_type:%s' % cat

    def __news_list_name(self):
        ''' 新闻Id 列表名称 '''
        return 'news'

    def get_news_number(self):
        return len(self.r.lrange(self.__news_list_name(), 0, -1))

    def add_news(self, news_obj):
        ''' 新增新闻数据 '''
        # 获取到新闻的Id
        int_id = self.r.incr('news_id')
        # 拼接新闻数据Hash key (news:id)
        news_id = self.__news_id(int_id)
        # 存储新闻数据(hash)   hash适合存储对象
        rest = self.r.hmset(news_id, news_obj)
        # 存储新闻的Id List  实现分页
        self.r.lpush(self.__news_list_name(), int_id)
        # 存储新闻的类别-新闻Id (set)
        self.r.sadd(self.__news_type(news_obj['news_type']), int_id)
        return rest

    def add_news_with_trans(self, news_obj):
        ''' 新增新闻+事务支持 '''
        pipe = self.r.pipeline()
        # 获取到新闻的Id
        int_id = self.r.incr('news_id')
        # 拼接新闻数据Hash key (news:id)
        news_id = self.__news_id(int_id)
        # 存储新闻数据(hash)   hash适合存储对象
        pipe.hmset(news_id, news_obj)
        # 存储新闻的Id List  实现分页
        pipe.lpush(self.__news_list_name(), int_id)
        # 存储新闻的类别-新闻Id (set)
        pipe.sadd(self.__news_type(news_obj['news_type']), int_id)
        rest = pipe.execute()
        return rest

    def get_all_news(self):
        ''' 获取所有的新闻数据 '''
        # 取所有的新闻id 从列表news中取
        id_list =self.r.lrange(self.__news_list_name(), 0, -1)
        news_list = []
        # 循环id列表，从hash news:id取出
        for int_id in id_list:
            # 新闻的hash中的field
            news_id = self.__news_id(int_id)
            # hgetall(self, name, key) "Return a Python dict of the hash's name/value pairs"
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)
        return news_list

    def get_news_from_id(self, int_id):
        ''' 根据新闻的ID来获取新闻数据 '''
        # 获取新闻key
        news_id = self.__news_id(int_id)
        # 查询新闻数据hash
        data = self.r.hgetall(news_id)
        data['id'] = int_id
        return data

    def get_news_from_cat(self, news_type):
        ''' 根据新闻的类别来查询新闻数据 '''
        news_list = []
        # 获取新闻列表的key
        news_type = self.__news_type(news_type)
        # 查询该列表下的所有新闻ID
        id_list = self.r.smembers(news_type)
        # 通过循环来查询新闻数据
        for int_id in id_list:
            news_id = self.__news_id(int_id)
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)
        return news_list

    def paginate(self, page=None, per_page=10):
        ''' 获取分页数据 '''
        if page is None:
            page = 1
        start = (page - 1) * per_page
        end = page * per_page - 1
        news_list = []

        # 查询该页的新闻ID
        id_list = self.r.lrange(self.__news_list_name(), start, end)
        for int_id in id_list:
            news_id = self.__news_id(int_id)
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)

        return Paginate(news_list, page, per_page)

    def update_news(self, int_id, news_obj):
        ''' 修改新闻数据 '''
        # 找到新闻的key(news:id)
        news_id = self.__news_id(int_id)
        # 设置hash的指
        return self.r.hmset(news_id, news_obj)

    def delete_news(self, int_id, news_obj):
        ''' 物理除新闻数据 '''
        # 拼接新闻的ID(news:id)
        news_id = self.__news_id(int_id)
        # 从列表中删除新闻数据 id
        self.r.lrem(self.__news_list_name(), int_id, 0)
        # 从set中删除对应的类别下的数据
        news_type = self.__news_type(news_obj['news_type'])
        self.r.srem(news_type, int_id)
        # 删除新闻的数据
        return self.r.hdel(news_id, *NEWS_FIELDS)

    def init_news(self, data_list):
        ''' 批量新增新闻 '''
        for news_obj in data_list:
            rest = self.add_news_with_trans(news_obj)
            print(rest)




































