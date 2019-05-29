Python操作MongoDB

MongoDB数据库介绍、安装配置、使用命令行操作数据库、图形化管理工具

MongoDB数据库介绍:
文档:
文档类似于关系库里的行
{"foo" : 3, "greeting" : "Hello, world!"}
区分大小写, key唯一，不可重复，键值对是有序的
集合:
集合就是一组文档
集合类似于关系库里的表
集合中的文档无需固定的结构

集合的命名
命名规则
1. 不能是空字符串("")
2. 不能包含\0字符(空字符）
3. 不能使用system.的前缀(系统保留)
4. 建议不包含保留字"$"
5. 用.分割不同命名空间的子集合(如: blog.users, blog.posts)

数据库:
1. 多个文档组成集合，多个集合组成数据库
2. 一个实例可以承载多个数据库
3. 每个数据库都有独立的权限(MYSQL数据库可以设置读、写、读写等权限)
4. 保留的数据库名称(admin, local, config),是系统自带的


BSON是由10gen开发的一个数据格式，目前主要用于MongoDB中，是MongoDB的数据存储格式
。BSON基于JSON格式，选择JSON进行改造的原因主要是JSON的通用性及JSON的schemaless的特性。


MongoDB安装和配置:
默认是localhost:27017

使用:
中文doc: https://www.yiibai.com/mongodb/
中英文doc: http://docs.mongoing.com/crud.html
查看数据库，创建/使用数据库dbname,查看集合
show dbs; use dbname;
show collections;
在 MongoDB 中，不需要创建集合。当插入一些文档时，MongoDB 会自动创建集合
db.newcollection.insert({"name" : "yiibaitutorials"})
查询所有数据
db.collectionname.find()
查询一条数据
db.collectionname.findOne():


更新文档:
更新 默认是更新一条复合条件的，可以加入{multi : true}多条更新
> db.students.find()
{ "_id" : ObjectId("5ced50be71b149e85ce3dd89"), "name" : "cla", "age" : 21 }
{ "_id" : ObjectId("5ced521771b149e85ce3dd8a"), "name" : "clarence", "age" : 12 }
{ "_id" : ObjectId("5ced53fa71b149e85ce3dd8b"), "name" : "Amy2", "age" : 16, "sex" : "male" }
> //这样更新会重新替换成新的对象
> db.students.update({name:"cla"}, {name:"clar"})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.students.find()
{ "_id" : ObjectId("5ced50be71b149e85ce3dd89"), "name" : "clar" }
{ "_id" : ObjectId("5ced521771b149e85ce3dd8a"), "name" : "clarence", "age" : 12 }
{ "_id" : ObjectId("5ced53fa71b149e85ce3dd8b"), "name" : "Amy2", "age" : 16, "sex" : "male" }
> //先查询到需要修改的数据对象，然后更新
> s = db.students.find({name:"clar"})
{ "_id" : ObjectId("5ced50be71b149e85ce3dd89"), "name" : "clar" }
> //执行更新操作 s.name = "clarenc"等等
> db.students.update({name:"cla"}, s)


删除文档:
remove([criteria,[justOne]])
criteria-可选，符合删除条件的集合将被删除
justOne-可选，如果设置为true或1,则只删除一个文档
eg:

> db.students.find()
{ "_id" : ObjectId("5ced521771b149e85ce3dd8a"), "name" : "clarence", "age" : 12 }
{ "_id" : ObjectId("5ced53fa71b149e85ce3dd8b"), "name" : "Amy2", "age" : 16, "sex" : "male" }
{ "_id" : ObjectId("5ced57c5199c55e2604848cd"), "name" : "clar" }
> db.students.remove({name:"clarence"})
WriteResult({ "nRemoved" : 1 })
> db.students.find()
{ "_id" : ObjectId("5ced53fa71b149e85ce3dd8b"), "name" : "Amy2", "age" : 16, "sex" : "male" }
{ "_id" : ObjectId("5ced57c5199c55e2604848cd"), "name" : "clar" }
> db.students.remove({}) //删除集合students中所有的文档
WriteResult({ "nRemoved" : 2 })
> db.students.find()


练习:
任务:
1. 创建一个学生信息表(至少包含: 姓名、性别、成绩、年龄)
2. 写入十五条不同的数据
3. 查询所有的男生数据(只需要学生的姓名和年龄)
4. 查询成绩及格的学生信息(学生成绩大于或等于60分)
5. 查询所有18岁的男生和16岁的女生的数据
6. 按照学生的年龄进行排序
7. 将所有的学生年龄增加一岁



















