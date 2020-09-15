#!usr/bin/python
# -*- coding:utf8 -*-
"""
# 需要权限认证的方式创建连接对象以及集合操作对象
from pymongo import MongoClient
from urllib.parse import quote_plus

user = 'python' # 账号
password = 'python' # 密码
host = '127.0.0.1' # host
port = 27017 # port
uri = "mongodb://%s:%s@%s" % (quote_plus(user),
                              quote_plus(password),
                              host)
# quote_plus函数：对url进行编码
# uri = mongodb://python:python@127.0.0.1
client = MongoClient(uri, port=port)
collection = client.db名.集合名
"""
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# collection = client['users']['stu']
collection = client.users.stu
print(collection)

# 添加一条数据
# res = collection.insert_one({"name": "张三", "age": 18})
# print(res)

# 插入多条数据
# data_list = [{"name": "小桂子"}, {"name": "小阳子"}, {"name": "刘欢"}]
# res = collection.insert_many(data_list)
# print(res)

# 查找数据
# res = collection.find({})
# for r in res:
#     print(r)

# 更新一条
# res = collection.update_one({"name": '刘欢欢'}, {"$set": {"name": "刘欢"}})
# print(res)

# 更新多条
# res = collection.update_many({}, {"$set": {"class": "python"}})
# print(res)

# res = collection.update_many({"class": "python"}, {"$set": {"age": 18}})
# print(res)

# 删除数据
res = collection.delete_one({"name": "刘欢"})
print(res)






















