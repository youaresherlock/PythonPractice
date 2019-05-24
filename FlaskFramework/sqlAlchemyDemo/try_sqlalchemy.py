#!usr/bin/python
# -*- coding:utf8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# The string form of the URL is dialect[+driver]://user:password@host/dbname[?key=value..]
# 'mysql://root:x1430371727@localhost:3306/news' 端口号默认可以不写
# encoding: Defaults to utf-8. This is the string encoding used by SQLAlchemy for string encode/decode operations which occur within SQLAlchemy, outside of the DBAPI.
engine = create_engine('mysql://root:x1430371727@localhost/news_test?charset=utf8', encoding="utf-8")
# we define a Session class which will serve as a factory for new Session objects
Session = sessionmaker(bind=engine)
Base = declarative_base()

class News(Base):
    # 数据库是news_test,数据库中表是news
    __tablename__ = "news"
    # id = Column("news_id",Integer, primary_key = True) 表中的id是news_id
    id = Column(Integer, primary_key = True)
    title = Column(String(200), nullable = False)
    content = Column(String(2000), nullable = False)
    type = Column(String(10), nullable = False)
    image = Column(String(300))
    author = Column(String(20),)
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

# 通过调用MetaData.create_all()方法，创建表
# Base.metadata.create_all(engine)

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    # 通过sqlalchemy将数据存入mysql出现乱码，可以设置引擎编码方式为utf8
    def add_one(self):
        ''' 新增记录 中文需要engine增加?charset=utf8'''
        new_obj = News(title = '标题', content = '内容', type = '百家')
        new_obj2 = News(title = 'title', content = 'content', type = '百家')
        self.session.add(new_obj)
        self.session.add(new_obj2)
        self.session.commit()
        return new_obj

    def add_more(self):
        new_obj = News(title='标题1', content='内容1', type='百家')
        new_obj2 = News(title='title2', content='content2', type='推荐')
        self.session.add_all([new_obj, new_obj2])
        self.session.commit()

    def get_one(self):
        ''' 查询一条数据 '''
        # https://docs.sqlalchemy.org/en/13/orm/query.html#the-query-object
        # Return the first result of this Query or None if the result doesn’t contain any row.
        return self.session.query(News).first()
        # 通过主键id获取
        # return self.session.query(News).get(1)

    def get_more(self):
        # apply the given filtering criterion to a copy of this Query, using keyword expression.
        return self.session.query(News).filter_by(is_valid = 1)
        # return self.session.query(News).all()

    def update_data(self, pk):
        ''' 修改指定id的数据'''
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 1
            self.session.commit()
            return True
        return False
        # ''' 根据筛选条件修改多条数据 '''
        # filter()和filter_by()区别
        # data_list = self.session.query(News).filter(News.id > 4)
        # # data_list = self.session.query(News).filter_by(is_valid = True)
        # for item in data_list:
        #     item.is_valid = 1
        # self.session.commit()

    def delete_data(self, pk):
        ''' 删除数据 '''
        # 获取要删除的数据
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            self.session.delete(new_obj)
            self.session.commit()

def main():
    obj = OrmTest()
    # rest = obj.add_one()
    # print(rest.id)

    # obj.add_more()

    # rest = obj.get_one()
    # if rest:
    #     print(f'ID:{rest.id}=>{rest.title}')
    # else:
    #     print("Not exist.")

    # rest = obj.get_more() print(rest.count())
    # for instance in obj.get_more():
    #     print(instance.id, instance.title)

    # print(obj.update_data(4))

    obj.delete_data(1)

if __name__ == '__main__':
    main()

































