##### �м��:

##### ����:
+ Django�е��м����һ�����������ײ�Ĳ��ϵͳ,���Խ���Django���������Ӧ�������,
�޸�Django����������
+ �м�������Ϊ�������ṩ��һ��������ʽ�Ŀ�����ʽ, ��ǿ��Django��ܵĽ�׳��, ������
MVCҲ��������� 

##### ʲô����������(AOP):
+ AOP��Aspect Oriented Programming����д���������������̡�����������ƽʱ�Ӵ�����OOP��
�Ǳ�̵Ĳ�ͬ˼�룬OOP��������������̡������ᳫ���ǽ�����ģ�黯�����󻯣���AOP��˼�룬
��̫һ�������ᳫ�������ͬһ�������ͳһ����ͨ��Ԥ���뷽ʽ�������ڶ�̬����ʵ�ֳ�����
��ͳһά����һ�ּ�����AOP��OOP������������������е�һ���ȵ㣬Ҳ��Spring����е�һ��
��Ҫ���ݣ��Ǻ���ʽ��̵�һ���������͡�����AOP���Զ�ҵ���߼��ĸ������ֽ��и��룬�Ӷ�ʹ
��ҵ���߼�������֮�����϶Ƚ��ͣ���߳���Ŀ������ԣ�ͬʱ����˿�����Ч�ʡ�

##### ʹ�ó���:
+ ��ĳЩ������ÿ���������Ӧʱ����ִ��ʱ,����д���м����
+ ����,ÿ�η���post����Ҫ����CSRF��֤, �Ͱ�CSRF��֤�Ĵ���д���м���� 
+ ��ȫ���û����У�顢ȫ���û�����Ƶ��У�顢�û����ʺ��������û����ʰ�����

##### ���˼��:
+ ���������̡����ֺ�ʽ��� 
+ ����ֱ���޸Ŀ��Դ��,�Ϳ��Դﵽ�Լ���Ҫ��ִ�н�� 

###### Ĭ���м��
```python 
# �м��
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Ϊ��֤��GET����(POST, PUT, DELETE)�����������գ����м����Ҫע�͵�
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""
class SecurityMiddleware 
The django.middleware.security.SecurityMiddleware provides several
security enhancements to the request/response cycle. Each one can 
be independently enabled or disabled with a setting.

class SessionMiddleware 
Enables session support.
# ��process_response��ʵ��
# ��session����д�뵽session��� request.session.save()
# ��session_keyд�뵽�������cookie�� response.set_cookie("sessionid":"session_key")

class CommonMiddleware 
Adds a few conveniences for perfectionists:

class CsrfViewMiddleware 
Before any view middleware that assumes that CSRF attacks have been dealt with.

AuthenticationMiddleware
uses session storage.
# ��process_request��ʵ��
# ��cookie�еõ�session_key, ��ȡsession�е�user_id

MessageMiddleware
After SessionMiddleware: can use session-based storage.

XFrameOptionsMiddleware
Simple clickjacking protection via the X-Frame-Options header.
"""
```

##### ʲô��CSRF����:
+ ��վ����α��(cross site request forgery) ָ�����ߵ����������ݣ���������巢�Ͷ�������
##### ��ֹCSRF����
+ �ڿͻ�����������������ݵ�ʱ�򣬺�˻�����Ӧ�е� cookie ������ csrf_token ��ֵ
+ �� Form �������һ�����صĵ��ֶΣ�ֵҲ�� csrf_token
+ ���û�����ύ��ʱ�򣬻����������ֵ���̨��������
+ ��˽��ܵ������Ի����¼����¼���
+ �� cookie ��ȡ�� csrf_token
+ �� ��������ȡ�������ص� csrf_token ��ֵ
+ Django ���жԱ� (����ĶԱȲ�Ҫ��һ��һ��, ��ʱ������ֵ��һ��)
+����Ա��ܹ�ͨ��, ��������������
+ ����ԱȲ��ܹ�ͨ�������������������󣬲�ִ����һ������
+ ���Ƿ��� csrf ���ֶ���Ҫ��: �� cookie ������ֵ, �ڱ���Ҳ����һ�������ֶ�, 
�������ֶ��ύ���жԱ�. �ж��Ƿ��Ǻ��������

##### �м������ 
1. init ��ʼ���м��ʱ,�Զ�����һ��
2. process_request(self, request): ����ս���, ִ����ͼ����֮ǰ����
3. process_view(self, request, view_func, view_args, view_kwargs):
    URL·��ƥ��ɹ���, ִ����ͼ����֮ǰ����, �õ���ͼ��������, �Լ����в���
4. process_template_response(self, request, response):
    ִ����render()��Ⱦ���������
5. process_exception(self, request, exception):
    ִ����ͼ�����������쳣ʱ����
6. process_response(self, request, response):
    ִ����ͼ����֮������Ӧʱ����

##### �м���Ķ��巽��
`����1`
```python
"""
����һ���м������������Ȼ�󷵻�һ�����Ա����õ��м����
�м������������Ҫ����һ�����Ե��õ� get_response ����
���ص��м��Ҳ��һ�����Ա����õĶ��󣬲�������ͼһ����Ҫ����һ�� request �������������һ�� response ����
"""
def simple_middleware(get_response):
    # �˴���д�Ĵ������ Django ��һ�����úͳ�ʼ����ʱ��ִ��һ�Ρ�

    def middleware(request):

        # �˴���д�Ĵ������ÿ����������ͼǰ�����á�

        response = get_response(request)

        # �˴���д�Ĵ������ÿ����������ͼ֮�󱻵��á�

        return response

    return middleware
```

`����2`
```python
"""
�м����һ��������Python�࣬���Զ���Django�ṩ�����������е�һ������
�ڹ��̸�Ŀ¼�£��½�middlewares.py�ļ����Զ����м��
�������Զ�����м���У���ȥʵ������Ҫ����������
"""
# �����м���ĸ���
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    """�Զ����м��"""
    def process_request(self, request):
        """��������ǰ�Զ�����"""
        print('process_request1 ������')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # ������ͼǰ�Զ�����
        print('process_view1 ������')

    def process_response(self, request, response):
        """��ÿ����Ӧ���ظ��ͻ���֮ǰ�Զ�����"""
        print('process_response1 ������')
        return response
```

##### �м����ִ��˳�� 
```text
����ͼ������ǰ(����)���м��������������ִ��
����ͼ�������(���)���м��������������ִ��

1. �Ȱ�������ִ��ÿ��ע���м����process_request����,process_request�������ص�
ֵ��None,������ִ��,������ص�ֵ��HttpResponse���󣬲���ִ�к����process_request
����,����ִ�е�ǰ��Ӧ�м����process_response����.
��1-6���м��,��3���м������HttpResponse���󣬽�����ִ��3��2��1��process_request����

2. ���process_request������None,��ִ�����ƥ��·�ɣ��ҵ�Ҫִ�е���ͼ�������Ȳ�
ִ����ͼ����,��ִ���м���е�process_view����,process_view��������None,������˳��ִ��,
���е�process_view����ִ�����ִ����ͼ����.�����м��3process_view����������HttpResponse
����,��4��5��6��process_view����ͼ��������ִ��, ֱ�Ӵ����һ���м��,Ҳ�����м��6��
process_response������ʼ����ִ�� e
```
















