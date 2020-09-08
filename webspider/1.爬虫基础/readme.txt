1.1 爬虫的概念和作用
    网络爬虫（又被称为网页蜘蛛，网络机器人）就是模拟客户端(主要指浏览器)发送网络请求
，接收请求响应，一种按照一定的规则，自动地抓取互联网信息的程序。


1.2 爬虫的分类和流程
爬虫的基本流程如下:
    获取一个 url 地址
    向目标 url 地址发送请求，并获取响应
    如果从响应中提取 url 地址，则继续发送请求获取响应
    如果从响应中提取数据，则将数据进行保存


1.3 Http协议的复习
200 OK
201 created
204 not content
301 moved permanently永久重定向
302 found临时重定向
400 Bad Request
401 Unauthorized
403 forbidden  请求资源的访问被服务器拒绝了
404 not found
405 method not allowed
500 internal server error
502 bad gateway
503 service unavailable


http以及https的概念和区别
HTTPS比HTTP更安全，但是性能更低
    HTTP：超文本传输协议，默认端口号是80
    超文本：是指超过文本，不仅限于文本；还包括图片、音频、视频等文件
    传输协议：是指使用共用约定的固定格式来传递转换成字符串的超文本内容
    HTTPS：HTTP + SSL(安全套接字层)，即带有安全套接字层的超本文传输协，默认端口号：443
    SSL对传输的内容（超文本，也就是请求体或响应体）进行加密
    可以打开浏览器访问一个url，右键检查，点击net work，点选一个url，查看http协议的形式























