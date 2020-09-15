mongodb:
Ĭ�϶˿�: 27017
Ĭ�������ļ���λ��: /etc/mongod.conf
Ĭ����־��λ��: /var/log/mongodb/mongod.log

���Է�ʽ����:
sudo service mongod start
sudo service mongod stop
sudo service mongod restart

�鿴�Ƿ������ɹ�:
ps aux | grep mongod

����mongodb�Ŀͻ���: ����mongo shell
�������ؿͻ���: mongo
�鿴����: mongo -help
�˳�: exit����ctrl+c

mongodb���ݿ������:
�鿴��ǰ�����ݿ�: db(û���л����ݿ�������Ĭ��ʹ��test���ݿ�)
�鿴���е����ݿ�: show dbs/show databases
�л����ݿ�: use db_name
ɾ����ǰ�����ݿ�: db.dropDatabase()

mongodb���ϵ�����:
�����ֶ���������, �򲻴��ڵļ����е�һ���������ʱ,���ϻ��Զ�����������
�ֶ���������: db.createCollection(name, options)
eg: db.createCollection('sub', {capped: true, size: 10})
�鿴����: show collections
ɾ������: db.��������.drop()
��鼯���Ƿ��趨����: db.��������.isCapped()

ע���:
ÿ���ĵ�����һ������,Ϊ_id,��֤ÿ���ĵ���Ψһ�ԣ�������.
����:
    4���ֽڵ�ʱ���
    3���ֽڵĻ���id
    2���ֽ�mongodb�ķ������id
    3���ֽڵ�����ֵ

mongodb��������:
db.��������.insert(document)  �����ָ��_id����,���Զ�����һ��Ψһ��ObjectId

mongodb�ı���:
db.��������.save(document) ����ĵ���_id�Ѿ��������޸�,���_id�����������

��ѯ:
db.��������.find() ��ѯȫ��
db.��������.find({�����ĵ�})
db.��������.findOne({�����ĵ�}) ֻ���ص�һ��
db.��������.find({�����ĵ�}).pretty() �������ʽ��, ���ܺ�findOne()һ��ʹ��

�Ƚ������:
$lt (less than) $lte (less than equal)
$gt (greater than) $gte
$ne (unequal)
��ѯ�������18������ѧ��
db.stu.find({age:{$gte:18}})

�߼������: ��/���߼�
and: ��json��д�����������
��ѯ������ڻ����18, �����Ա�Ϊtrue��ѧ��
db.stu.find({age:{$gt:18},gender:true})
or: ֵΪ����
��ѯ�������18, ���Ա�Ϊfalse��ѧ��
db.stu.find({$or:[{age:{$gt:18}},{gender:false}]}

��Χ�����:
$in/$nin �ж������Ƿ���ĳ��������
��ѯ����Ϊ18��28��ѧ��
db.stu.find({age:{$in:[18,28]}})

֧��������ʽ: $regex ���ַ�ʽ
��ѯname��'��'��ͷ������
db.stu.find({name:{$regex:'^��'}})
db.stu.find({name:/^��/}}

�Զ����ѯ:
mongo shell ��һ��js��ִ�л��� ʹ��$where дһ�������� ������������������
��ѯ�������30��ѧ��
db.stu.find({
 $where:function() {
     return this.age>30;}
})

skip(����ָ���������ĵ�)��limit(��ȡָ���������ĵ�):
db.��������.find().skip(number).limit(number)

ͶӰ:
�ڲ�ѯ���ķ��ؽ����,ֻѡ���Ҫ���ֶ�
db.��������.find({}, {�ֶ�����:1,...}) ֵΪ1��ʾ��ʾ,ֵΪ0����ʾ _idĬ������ʾ��
db.stu.find({}, {_id:0,name:1,gender:1}) ֻ��ʾname��gender

����sort:
db.��������.find().sort({�ֶ�:1,...})
����1����,-1Ϊ����
�����Ա���,�ٸ�����������
db.stu.find().sort({gender:-1,age:1})

ͳ�Ƹ���count:
db.��������.find({����}).count()/db.��������.count({����})

mongodb�ĸ���:
db.��������.update({query}, {update}, {multi: boolean})
query: ��ѯ����
update: ���²�����
multi: Ĭ����false, ��ʾֻ�����ҵ��ĵ�һ������
db.stu.update({name:'hr'},{name:'mnc'})           # ȫ�ĵ����и��Ǹ���
db.stu.update({name:'hr'},{$set:{name:'hys'}})    # ָ����ֵ���²���
db.stu.update({},{$set:{gender:0}},{multi:true})  # ����ȫ��
multi�����$setһ��ʹ��

mongodb��ɾ��:
db.��������.remove({query}, {justOne: boolean})
query:��ѡ��ɾ�����ĵ�������
justOne:��ѡ�� �����Ϊtrue��1����ֻɾ��һ����Ĭ��false����ʾɾ��ȫ��

�ۺ�:
db.stu.aggregate(
     {$match:{age:{$gt:20}},
     {$group:{_id:"$gender",counter:{$sum:1}}}
     )
_id��ʾ���ĸ��ֶη�������

��������
    �ӿ��ѯ�ٶ�
    �������ݵ�ȥ��
ensureIndex/createIndex
db.������.ensureIndex({����:1}), 1��ʾ����,-1��ʾ����
ɾ������
db.������.dropIndex({'��������':1}}
�鿴����
db.������.getIndexes()
���Ψһ�������﷨:
db.����.ensureIndex({"�ֶ���":1}, {"unique":true})
����Ψһ������������ȥ��:
����Ψһ����ָ�����ֶε�ֵ,�����ͬ,���޷���������













