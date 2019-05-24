#!usr/bin/python
# -*- coding:utf8 -*-

import MySQLdb

class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host = '127.0.0.1',
                user = 'root',
                passwd = 'x1430371727',
                db = 'news',
                port = 3306,
                charset = 'utf8'
            )
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def close_conn(self):
        try:
            if self.conn:
                # 关闭连接
                 self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    # 获取一条
    def get_one(self):
        sql = "SELECT * FROM `news` WHERE `news_type` = %s ORDER BY `created_at` DESC;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ('百家', ))
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        print(cursor.fetchone())
        cursor.close()
        self.close_conn()
        return rest

    # 查询多条
    def get_more(self):
        sql = "SELECT * FROM `news` WHERE `news_type` = %s ORDER BY `created_at` DESC;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ('百家', ))
        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        # cursor.fetchall()是以一个元组组成的元组列表, rest为字典组成的列表
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

    # 分页查询 获取第page页的page_size条数据
    def get_by_paging(self, page, page_size):
        offset = (page - 1) * page_size
        sql = "SELECT * FROM `news` WHERE `news_type` = %s ORDER BY `created_at` DESC LIMIT %s, %s;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ('百家', offset, page_size))
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

    # 增加一条数据
    def add_one(self):
        sql = "INSERT INTO `news`(`title`, `img_url`, `content`, `news_type`, `is_valid`) VALUE(" \
              "%s, %s, %s, %s, %s);"
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, ('标题3', '/static/img/news/03.png', '新闻内容3', '推荐', 1))
            # self.conn.rollback()
            # 提交事务
            self.conn.commit()
            cursor.close()
        except MySQLdb.Error as e:
            print("Error")
            self.conn.rollback() # 出现异常，回滚
        finally:
            self.close_conn()

def main():
    obj = MysqlSearch()
    # rest = obj.get_one()
    # print(rest)

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)

    # rest = obj.get_by_paging(2, 4)
    # for item in rest:
    #     print(item)

    obj.add_one()

if __name__ == "__main__":
    main()





















