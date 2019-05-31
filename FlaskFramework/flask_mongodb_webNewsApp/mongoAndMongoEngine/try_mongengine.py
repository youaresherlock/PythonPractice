#!usr/bin/python
# -*- coding:utf8 -*-
from mongoengine import connect
from mongoengine import Document, StringField, IntField, FloatField,\
    EmbeddedDocumentField, EmbeddedDocument, ListField


# connect('students')
connect('students', host='127.0.0.1', port=27017)
# connect('students', host='mongodb://localhost/students')

# Can either be nested tuples of value (stored in mongo) and a human readable key
SEX_CHOICES = (
    ('male', '男'),
    ('female', '女')
)

class Grade(EmbeddedDocument):
    ''' 成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)

class Student(Document):
    ''' 学生 '''
    # mongodb这里默认以_id作为主键
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(required=True, choices=SEX_CHOICES)
    grades  = ListField(EmbeddedDocumentField(Grade))
    address = StringField(max_length=32, required=True)
    school = StringField()

    # meta定义数据库中文档类使用的集合名字,可以是新的集合名称也可以是已经存在的集合名称
    # 集合的名称默认是类的名称，转换成小写,比如此类默认集合名称为student
    meta = {
        "collection" : "students2",
        #http://docs.mongoengine.org/guide/defining-documents.html?highlight=meta#ordering 将结果集会自动根据age排序
        "ordering" : ['-age']
    }

class TestMongoEngine(object):

    def add_one(self):
        ''' 新增数据 '''
        data_science = Grade(name="数据分析", score=10)
        english = Grade(name="英语", score=89)
        student = Student(name="bob", age=32, sex="male", address="中国", grades=[data_science, english])
        student.save()
        return student

    def get_one(self):
        ''' 查询一条数据 '''
        # Student.objects是querySet,此对象有first()方法, 返回结果集中的第一个对象
        return Student.objects.first()

    def get_all(self):
        ''' 查询所有数据 '''
        # Returns a copy of the current QuerySet.
        return Student.objects.all()

    def get_from_oid(self, oid):
        ''' 根据id来获取数据 '''
        return Student.objects.filter(pk=oid).first()

    def update(self):
        ''' 修改数据 '''
        # 修改一条数据
        # return Student.objects.filter(address="日本").update_one(inc__age=10)
        # 修改多条数据
        return Student.objects.filter(sex="male").update(inc__age=1)

    def delete(self):
        ''' 删除数据 '''
        # 删除一条数据
        # Document update()   Delete the documents matched by the query.
        # return Student.objects.filter(address="日本").first().delete()
        # 删除多条数据
        return Student.objects.filter(address="日本").delete()


def main():
    obj = TestMongoEngine()
    name, score = "name", "score"
    # result = obj.add_one()
    # print(result.id, result.pk)

    # result = obj.get_one()
    # print(f"id: {result.id}, name: {result.name}, grades: {[{name: grade.name, score: grade.score} for grade in result.grades]}")

    result = obj.get_all()
    for each in result:
        print(f"id: {each.id}, name: {each.name}, grades: {[{name: grade.name, score: grade.score} for grade in each.grades ]}")

    # result = obj.get_from_oid("5cef8ea5d97e529ea24c0286")
    # if result:
    #     print(f"id: {result.id}, name: {result.name}, grades: {[{name: grade.name, score: grade.score} for grade in result.grades]}")

    # obj.update()

    # obj.delete()

if __name__ == "__main__":
    main()