Python GIL(Global Interpreter Lockȫ�ֽ�������)
Python���߳�,��װ�˵ײ�Ĳ���ϵͳ�߳�,��Linuxϵͳ����Pthread(ȫ��Ϊ
POSIX Thread), ����Windowsϵͳ����Windows Thread. ����,Python���߳�,
Ҳ��ȫ�ܲ���ϵͳ����,����Э����ʱִ�С������ڴ���Դ�������жϵȵ�

CPython����GIL��ʵ��Ҫ������ԭ��:
    1. Ϊ�˹���������ڴ���������ĸ��ӵľ�����������(race condition)
    2. ��ΪCPython����ʹ��C���Կ�,���󲿷�c���Կⶼ����ԭ���̰߳�ȫ��(�̰߳�ȫ
�ή�����ܺ����Ӹ��Ӷ�)

�ƹ�GIL:
    1. ʹ��JPython(Javaʵ�ֵ�Python������)
    2. �ѹؼ����ܴ���,�ŵ��������(һ����C++)��ʵ�� 












