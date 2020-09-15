mongodb:
默认端口: 27017
默认配置文件的位置: /etc/mongod.conf
默认日志的位置: /var/log/mongodb/mongod.log

测试方式启动:
sudo service mongod start
sudo service mongod stop
sudo service mongod restart

查看是否启动成功:
ps aux | grep mongod

启动mongodb的客户端: 进入mongo shell
启动本地客户端: mongo
查看帮助: mongo -help
退出: exit或者ctrl+c

mongodb数据库的命令:
查看当前的数据库: db(没有切换数据库的情况下默认使用test数据库)
查看所有的数据库: show dbs/show databases
切换数据库: use db_name
删除当前的数据库: db.dropDatabase()

mongodb集合的命令:
无需手动创建集合, 向不存在的集合中第一次添加数据时,集合会自动被创建出来
手动创建集合: db.createCollection(name, options)
eg: db.createCollection('sub', {capped: true, size: 10})
查看集合: show collections
删除集合: db.集合名称.drop()
检查集合是否设定上限: db.集合名称.isCapped()

注意点:
每个文档都有一个属性,为_id,保证每个文档的唯一性，是主键.
构成:
    4个字节的时间戳
    3个字节的机器id
    2个字节mongodb的服务进程id
    3个字节的增量值

mongodb插入数据:
db.集合名称.insert(document)  如果不指定_id参数,会自动分配一个唯一的ObjectId

mongodb的保存:
db.集合名称.save(document) 如果文档的_id已经存在则修改,如果_id不存在则添加

查询:
db.集合名称.find() 查询全部
db.集合名称.find({条件文档})
db.集合名称.findOne({条件文档}) 只返回第一个
db.集合名称.find({条件文档}).pretty() 将结果格式化, 不能和findOne()一起使用

比较运算符:
$lt (less than) $lte (less than equal)
$gt (greater than) $gte
$ne (unequal)
查询年龄大于18的所有学生
db.stu.find({age:{$gte:18}})

逻辑运算符: 与/或逻辑
and: 在json中写多个条件即可
查询年龄大于或等于18, 并且性别为true的学生
db.stu.find({age:{$gt:18},gender:true})
or: 值为数组
查询年龄大于18, 或性别为false的学生
db.stu.find({$or:[{age:{$gt:18}},{gender:false}]}

范围运算符:
$in/$nin 判断数据是否在某个数组内
查询年龄为18、28的学生
db.stu.find({age:{$in:[18,28]}})

支持正则表达式: $regex 两种方式
查询name以'黄'开头的数据
db.stu.find({name:{$regex:'^黄'}})
db.stu.find({name:/^黄/}}

自定义查询:
mongo shell 是一个js的执行环境 使用$where 写一个函数， 返回满足条件的数据
查询年龄大于30的学生
db.stu.find({
 $where:function() {
     return this.age>30;}
})

skip(跳过指定数量的文档)和limit(读取指定数量的文档):
db.集合名称.find().skip(number).limit(number)

投影:
在查询到的返回结果中,只选择必要的字段
db.集合名称.find({}, {字段名称:1,...}) 值为1表示显示,值为0不显示 _id默认是显示的
db.stu.find({}, {_id:0,name:1,gender:1}) 只显示name和gender

排序sort:
db.集合名称.find().sort({字段:1,...})
参数1升序,-1为降序
根据性别降序,再根据年龄升序
db.stu.find().sort({gender:-1,age:1})

统计个数count:
db.集合名称.find({条件}).count()/db.集合名称.count({条件})

mongodb的更新:
db.集合名称.update({query}, {update}, {multi: boolean})
query: 查询条件
update: 更新操作符
multi: 默认是false, 表示只更新找到的第一条数据
db.stu.update({name:'hr'},{name:'mnc'})           # 全文档进行覆盖更新
db.stu.update({name:'hr'},{$set:{name:'hys'}})    # 指定键值更新操作
db.stu.update({},{$set:{gender:0}},{multi:true})  # 更新全部
multi必须和$set一起使用

mongodb的删除:
db.集合名称.remove({query}, {justOne: boolean})
query:可选，删除的文档的条件
justOne:可选， 如果设为true或1，则只删除一条，默认false，表示删除全部

聚合:
db.stu.aggregate(
     {$match:{age:{$gt:20}},
     {$group:{_id:"$gender",counter:{$sum:1}}}
     )
_id表示对哪个字段分组依据

创建索引
    加快查询速度
    进行数据的去重
ensureIndex/createIndex
db.集合名.ensureIndex({属性:1}), 1表示升序,-1表示降序
删除索引
db.集合名.dropIndex({'索引名称':1}}
查看索引
db.集合名.getIndexes()
添加唯一索引的语法:
db.集合.ensureIndex({"字段名":1}, {"unique":true})
利用唯一索引进行数据去重:
根据唯一索引指定的字段的值,如果相同,则无法插入数据













