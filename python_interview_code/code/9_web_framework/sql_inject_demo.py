#!usr/bin/python
# -*- coding:utf8 -*-

"""
CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id`)
);

insert into users (name,email,password) values ('laowang','laowang@qq.com',md5('laowang123'));
insert into users (name,email,password) values ('zhangsan','zhangsan@qq.com',md5('zhangsan123'));
insert into users (name,email,password) values ('lisi','lisi@gmail.com',md5('lisi123'));
"""
# sql 注入演示代码
import os 
import MySQLdb # pip install mysqlclient 

db = MySQLdb.connect(
    host="localhost", 
    user="root", 
    # passwd=os.getenv('MYSQL_PASS'),
    passwd='x1430371727',
    db="test"
)

cur = db.cursor() 

name = input('Enter name: ')
print('您输入的用户name是: {}'.format(name))
password = input('Enter password: ')    #
print('您输入的密码是: {}'.format(password))
# 直接拼接 sql 参数
# sql = "SELECT * FROM users WHERE name='"+name+"'" + " AND password=md5('"+password+"')"
sql = "SELECT * from users WHERE name=%s and password=md5(%s)"
print(sql)
# cur.execute(sql)
cur.execute(sql, (name, password))
for row in cur.fetchall():
    print('查询结果:', row)

db.close()
