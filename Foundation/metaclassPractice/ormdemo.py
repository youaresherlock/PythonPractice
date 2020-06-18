#!usr/bin/python
# -*- coding:utf8 -*-


# 实现ORM
# 定义Field类, 它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        # 对象的父类名:字段名
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field基础上, 定义各种类型 如StringField, IntegerField等
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 定义一个元类
class ModelMetaclass(type):
    """
    cls: 动态修改的类
    name: 动态修改的类名
    bases: 代表被动态修改的类的所有父类
    attr: 代表被动态修改的类的所有属性、方法组成的字典
    """
    def __new__(cls, name, bases, attrs):
        print("-"*20, name, bases, attrs)
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        # 假设表名和类名一致
        # attrs['__table__'] = name
        attrs['__table__'] = attrs.get('Meta').table
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        print('**kw', kw)
        super(Model, self).__init__(**kw)

    # 调用对象.key的时候触发
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    class Meta:
        table = "user"


# 创建一个实例
user = User(id=1, name='Clarence', email='test@orm.org', password='123')
# 保存到数据库
user.save()





















