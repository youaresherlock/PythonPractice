tornado框架
使用Python编写的网络框架和高性能的异步网络苦
适用于大量连接、长轮询、WebSockets应用

优势:
微框架、高性能  异步支持
缺点:
轮子少、不像Django、Flask等框架有大量插件支持
缺少最佳实践、使用的公司不多，学习资料少

使用场景:
构建微服务
    不适合复杂的CMS(内容管理系统)应用
    适合构建网站或者APP后端微服务

安装:
pip 安装或源码安装
pip isntall tornado python解释器里: import tornado; tornado.version

Tornado web主要模块
    tornado.web Application和RequestHandler类处理http请求
    tornado.template模板渲染
    tornado.routing处理路由

http服务器和客户端模块:
    tornado.httpserver 非阻塞HTTP服务器
    tornado.httpclient 异步HTTP客户端












