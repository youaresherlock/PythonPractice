#!usr/bin/python
# -*- coding:utf8 -*-
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient


class TestMongo(object):

    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.blog # self.client["blog"]

    def add_one(self):
        """ 新增数据 """
        post = {
            'title': '新的标题',
            'content': '博客内容,....',
            'created_at': datetime.now()
        }
        return self.db.blog.posts.insert_one(post)

    def add_many(self):
        ''' 新增多条数据 '''
        return self.db.blog.posts.insert_many([{'title': '标题', 'content':'内容',
            'created_at': datetime.now(), 'x': i} for i in range(0,10)])

    def get_one(self):
        ''' 查询一条数据 '''
        return self.db.blog.posts.find_one()

    def get_one_from_oid(self, oid):
        ''' 查询指定id的数据 '''
        return self.db.blog.posts.find_one({'_id': ObjectId(oid)})

    def get_more(self):
        ''' 查询多条数据 '''
        return self.db.blog.posts.find({'x':2})

    def update(self):
        ''' 修改数据 '''
        # 修改一条数据
        # result = self.db.blog.posts.update_one({'x' : 9}, {'$inc': {'x': 10}})
        # 修改多条数据
        result = self.db.blog.posts.update_many({}, {'$inc': {'x' : 10}})
        return result

    def delete(self):
        ''' 删除多条数据 '''
        # 删除一条数据
        # result = self.db.blog.posts.delete_one({'x' : 12})
        # 删除多条数据
        result = self.db.blog.posts.delete_many({'x': 12})
        return result
def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest.inserted_id)

    # obj.add_many()

    # rest = obj.get_one()
    # print(rest)

    # rest = obj.get_one_from_oid("5cee4ca722b9df7c751a1779")
    # print(rest)

    # posts = obj.get_more()
    # for each in posts:
    #     print(each)

    # rest = obj.update()
    # print(rest.matched_count)
    # print(rest.modified_count)

    # rest = obj.delete()
    # print(rest.deleted_count)


if __name__ == "__main__":
    main()
































