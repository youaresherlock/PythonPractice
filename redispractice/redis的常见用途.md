redis�Ǽ�ֵ�Ե����ݿ�,���õ�������������Ϊ�ַ�������(string),ɢ������(hash),�б�����(list),
��������(set), ���򼯺�����(zset)

Redis��������,��Ҫ����;��: ������,�߲���, ��Ϊ�ڴ���Ȼ֧�ָ߲���

1. �ֲ�ʽ��(string)��
setnx key value�� ��key������ʱ,��key��ֵ��Ϊvalue,����1. ��������key�Ѿ�����,
��setnx�����κζ���,����0 

��setnx����1ʱ,��ʾ��ȡ��, ��������Ժ�del key,��ʾ�ͷ���,���setnx����0��ʾ��ȡ��ʧ��, 
����˼·��ž������� 

2. ������(string)
��֪��ÿ������ı���������� 
set key 0
incr key // incr readcount::{����id} ÿ�Ķ�һ��
get key // get readcount::{����id} ��ȡ�Ķ���

3. ��Ϣ����(list)
һֱ��list��߷�
lpush key value 
key���list��Ԫ��ʱ��ֱ�ӵ�����û��Ԫ�ر�������ֱ���ȴ���ʱ���ֿɵ���Ԫ��Ϊֹ���������ӳ�ʱʱ��Ϊ10s
brpop key value 10 

4. ���а�(zset) 
redis��zset���������������а�ġ������б�ȥ�ء���ʷ��¼��ҵ������

ZREVRANGE key start stop [WITHSCORES]
�������� key �У�ָ�������ڵĳ�Ա��
*user1���û�����Ϊ 10*
zadd ranking 10 user1
zadd ranking 20 user2

# ȡ������ߵ�3���û�
zrevrange ranking 0 2 withscores























