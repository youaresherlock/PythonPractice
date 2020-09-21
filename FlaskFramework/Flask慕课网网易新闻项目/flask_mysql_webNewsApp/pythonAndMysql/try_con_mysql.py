#!usr/bin/python
# -*- coding:utf8 -*-

import MySQLdb

# 注: mysql8.x报错，因为版本默认的加密方式都改为了caching_sha2_password,可以改为mysql_native_password
# 获取连接
try:
    conn = MySQLdb.connect(
        host = '127.0.0.1',
        user = 'root',
        passwd = 'x1430371727',
        db = 'news',
        port = 3306,
        charset = 'utf8'
    )

    # 获取数据
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `news` ORDER BY `created_at` DESC")
    rest = cursor.fetchall()
    print(rest)

    # 关闭连接
    conn.close()
except MySQLdb.Error as e:
    print("Error: %s" % e)





















