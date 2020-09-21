ORM
对象关系映射(Object Relational Mapping, 简称ORM)模式是一种为了解决面向对象
与关系数据库存在的互不匹配的现象的技术.简单的说，ORM是通过使用描述对象和数据库之间
映射的元数据，将程序中的对象自动持久化到关系数据库中.

ORM提供了实现持久化层的另一种模式，它采用映射元数据来描述对象关系的映射,使得ORM中间件
能在任何一个应用的业务逻辑层和数据库层之间充当桥梁.Java典型的ORM中间件有: Hibernate,ibatis,
speedframework.


关系型数据库和实体间做映射，操作对象的属性和方法，跳过SQL语句

优点:
专用、庞大的数据库访问层可能不再需要、提高效率
像操作对象一样提取数据

缺点:
固定思维模式、牺牲执行效率
很可能将全部数据提取到内存对象中，持久化所有属性---不希望

python主要的库
1. SqlObject
2. peewee
3. Django's ORM
4. SQLAlchemy

SQLAlchemy
常见类型
https://docs.sqlalchemy.org/en/13/core/type_basics.html
Integer/Float/Boolean/ForeginKey/Date/DateTime/String





















