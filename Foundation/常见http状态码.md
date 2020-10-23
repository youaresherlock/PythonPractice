HTTP Status Code�����Ա�ʾ��ҳ������HTTP��Ӧ״̬��3λ���ִ���

200 OK �������ɹ������û����������
201 created �û��½����޸����ݳɹ�
202 Accept ��ʾ�����ѽ����̨�Ŷ�
204 not content 
301 moved permanently�����ض���
302 found��ʱ�ض��� 
400 Bad Request �û������������д���
401 Unauthorized  �û�û��Ȩ��
403 forbidden  ������Դ�ķ��ʱ��������ܾ��� ���ʱ���ֹ��
404 not found ������Ե��ǲ����ڵļ�¼
405 method not allowed 
406 Not Acceptable ������Եĸ�ʽ����ȷ
500 internal server error ��������������
502 bad gateway 
503 service unavailable 


200 OK
The request has succeeded. ����ɹ�

201 created
The request has succeeded and a new resource has been created
as a result. This is typically the response sent after POST
requests, or some PUT requests.
����ɹ����µ���Դ��������POST��PUT�������Ӧ

204 NO Content
There is no content to send for this request, but the headers may
be useful. The user-agent may update its cached headers for this
resource with the new ones.

301 Moved Permanently �����ض���
The URL of the requested resource has been changed permanently.
The new URL is given in the response.

302 Found
This response code means that the URI of requested resource
has been changed temporarily. Further changes in the URI
might be made in the future. Therefore, this same URI should
be used by the client in future requests.

400 Bad Request
The server could not understand the request due to invalid syntax.

401 Unauthorized
Although the HTTP standard specifies "unauthorized", semantically
this response means "unauthenticated". That is, the client must
authenticate itself to get the requested response.

403 Forbidden
The client does not have access rights to the content;that is, it is
unauthorized, so the server is refusing to give the requested resource.
Unlike 401, the client's identity is known to the server.

404 Not Found.
The server can not find the requested resource. In the browser,
this means the URL is not recognized.

405 Method Not Allowed
The request method is known by the server but has been disabled and
cannot be used.


500 Internal Server Error
The server has encountered a situation it doesn't know how to handle.

502 Bad Gateway
This error response means that the server, while working as a gateway
to get a response needed to handle the request, got an invalid response.

503 Service Unavailable
The server is not ready to handle the request.















