MongoDB ODM

1. MongoEngine安装及连接
2. ODM模型介绍
3. 通过ODM CURD

两种和数据库交互的方式
1. 使用原生语言查询 eg: select * from xxx...
2. 使用ODM/ORM(Object Document Model("ODM")/Object Relational Model("ORM")
,也就是对象关系映射和对象文档映射,表示把数据当做js对象，然后把它映射到低层数据库，
一些ORM与特定数据库绑定，而其他ORM则提供与数据库无关的后端

使用SQL或数据库支持的查询语言可以获得最佳性能

区别:
An ORM maps between an Object Model and a Relational Database.
An ODM maps between an Object Model and a Document Database.


1. 安装及连接:
文档:
pypi: https://pypi.org/project/mongoengine/
doc: https://mongoengine-odm.readthedocs.io/
安装:
pip install mongoengine


连接MongoDB:
To connect to a running instance of mongod, use the connect() function.
The first argument is the name of the database to connect to:
方式一: 简写 默认端口和地址为localhost:27017
方式二: 指定端口和地址
connect('students', host='127.0.0.1', port=27017)
方式三: 使用URI  connect('project1', host='mongodb://localhost/database_name')
connect('students', host = 'mongodb://localhost/students')
如果需要认证连接如下:
If the database requires authentication, username, password and authentication_source arguments should be provided:
connect('project1', username='webapp', password='pwd123', authentication_source='admin')
connect('database_name', host = 'mongodb://username:password@localhost/database_name')


2. ODM模型介绍
常见类型
StringField ObjectIdField IntField FloatField
DecimalField BooleanField DataTimeField ListField

关于mongoengine中的操作运算符可以查看
http://docs.mongoengine.org/guide/querying.html?highlight=operators
http://docs.mongoengine.org/guide/querying.html?highlight=operators#atomic-updates
中有inc-increment a value by a given amount 可以增加指定文档的字段值



















