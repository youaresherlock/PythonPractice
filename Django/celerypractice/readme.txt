celery:
    �ֲ�ʽ�������,�ܹ��ǱȽϵ��͵�������������ģ��. ��������Ŀͻ�����������,
ÿһ����������һ�������̸����������,ͬʱ��һ�������ӽ��̸���ִ������.
client��worker֮�����Ϣ����ͨ��broker, celery��broker�����ڵ���������Ϣ
����,��redis,rabbitMQ��.
Celery�ļܹ�:
    �����������,��Ϣ�м��(message broker),����ִ�е�Ԫ(worker)������ִ�н��
�洢(task result store)���
choose a broker:
    rabbitmq��redis

celery�Ĺ���ģʽ:

Э��ģʽ:
celery -A tasks worker -l info -P eventlet -E

celery -A celery_tasks.main worker -l info -P eventlet -c 1000