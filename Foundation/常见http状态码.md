HTTP Status Code是用以表示网页服务器HTTP响应状态的3位数字代码

200 OK 服务器成功返回用户请求的数据
201 created 用户新建或修改数据成功
202 Accept 表示请求已进入后台排队
204 not content 
301 moved permanently永久重定向
302 found临时重定向 
400 Bad Request 用户发出的请求有错误
401 Unauthorized  用户没有权限
403 forbidden  请求资源的访问被服务器拒绝了 访问被禁止了
404 not found 请求针对的是不存在的记录
405 method not allowed 
406 Not Acceptable 请求针对的格式不正确
500 internal server error 服务器发生错误
502 bad gateway 
503 service unavailable 


200 OK
The request has succeeded. 请求成功

201 created
The request has succeeded and a new resource has been created
as a result. This is typically the response sent after POST
requests, or some PUT requests.
请求成功，新的资源被创建。POST和PUT请求的响应

204 NO Content
There is no content to send for this request, but the headers may
be useful. The user-agent may update its cached headers for this
resource with the new ones.

301 Moved Permanently 永久重定向
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















