##### 中间件:

##### 概念:
+ Django中的中间件是一个轻量级、底层的插件系统,可以介入Django的请求和响应处理过程,
修改Django的输入或输出
+ 中间件的设计为开发者提供了一种无侵入式的开发方式, 增强了Django框架的健壮性, 其他的
MVC也有这个功能 

##### 什么是面向切面(AOP):
+ AOP是Aspect Oriented Programming的缩写，即『面向切面编程』。它和我们平时接触到的OOP都
是编程的不同思想，OOP，即『面向对象编程』，它提倡的是将功能模块化，对象化，而AOP的思想，
则不太一样，它提倡的是针对同一类问题的统一处理，通过预编译方式和运行期动态代理实现程序功能
的统一维护的一种技术。AOP是OOP的延续，是软件开发中的一个热点，也是Spring框架中的一个
重要内容，是函数式编程的一种衍生范型。利用AOP可以对业务逻辑的各个部分进行隔离，从而使
得业务逻辑各部分之间的耦合度降低，提高程序的可重用性，同时提高了开发的效率。

##### 使用场景:
+ 当某些操作在每次请求或响应时都会执行时,可以写在中间件中
+ 比如,每次发送post请求都要进行CSRF验证, 就把CSRF验证的代码写在中间件中 
+ 如全局用户身份校验、全局用户访问频率校验、用户访问黑名单、用户访问白名单

##### 设计思想:
+ 面向切面编程、无侵害式编程 
+ 不用直接修改框架源码,就可以达到自己想要的执行结果 

###### 默认中间件
```python 
# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 为保证非GET请求(POST, PUT, DELETE)可以正常接收，该中间件需要注释掉
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
# 在process_response中实现
# 将session数据写入到session后端 request.session.save()
# 将session_key写入到浏览器的cookie中 response.set_cookie("sessionid":"session_key")

class CommonMiddleware 
Adds a few conveniences for perfectionists:

class CsrfViewMiddleware 
Before any view middleware that assumes that CSRF attacks have been dealt with.

AuthenticationMiddleware
uses session storage.
# 在process_request中实现
# 从cookie中得到session_key, 再取session中的user_id

MessageMiddleware
After SessionMiddleware: can use session-based storage.

XFrameOptionsMiddleware
Simple clickjacking protection via the X-Frame-Options header.
"""
```

##### 什么是CSRF攻击:
+ 跨站请求伪造(cross site request forgery) 指攻击者盗用了你的身份，以你的名义发送恶意请求。
##### 防止CSRF攻击
+ 在客户端向后端请求界面数据的时候，后端会往响应中的 cookie 中设置 csrf_token 的值
+ 在 Form 表单中添加一个隐藏的的字段，值也是 csrf_token
+ 在用户点击提交的时候，会带上这两个值向后台发起请求
+ 后端接受到请求，以会以下几件事件：
+ 从 cookie 中取出 csrf_token
+ 从 表单数据中取出来隐藏的 csrf_token 的值
+ Django 进行对比 (这里的对比不要求一定一致, 有时候两个值不一致)
+如果对比能够通过, 则是正常的请求
+ 如果对比不能够通过，代表不是正常的请求，不执行下一步操作
+ 我们防护 csrf 的手段主要是: 在 cookie 中设置值, 在表单中也设置一个隐藏字段, 
把两个字段提交进行对比. 判断是否是合理的请求

##### 中间件方法 
1. init 初始化中间件时,自动调用一次
2. process_request(self, request): 请求刚进来, 执行视图函数之前调用
3. process_view(self, request, view_func, view_args, view_kwargs):
    URL路由匹配成功后, 执行视图函数之前调用, 拿到视图函数对象, 以及所有参数
4. process_template_response(self, request, response):
    执行了render()渲染方法后调用
5. process_exception(self, request, exception):
    执行视图函数中遇到异常时调用
6. process_response(self, request, response):
    执行视图函数之后有响应时调用

##### 中间件的定义方法
`方法1`
```python
"""
定义一个中间件工厂函数，然后返回一个可以被调用的中间件。
中间件工厂函数需要接收一个可以调用的 get_response 对象。
返回的中间件也是一个可以被调用的对象，并且像视图一样需要接收一个 request 对象参数，返回一个 response 对象。
"""
def simple_middleware(get_response):
    # 此处编写的代码仅在 Django 第一次配置和初始化的时候执行一次。

    def middleware(request):

        # 此处编写的代码会在每个请求处理视图前被调用。

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。

        return response

    return middleware
```

`方法2`
```python
"""
中间件是一个独立的Python类，可以定义Django提供的六个方法中的一个或多个
在工程根目录下，新建middlewares.py文件来自定义中间件
我们在自定义的中间件中，会去实现最重要的三个方法
"""
# 导入中间件的父类
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    """自定义中间件"""
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1 被调用')
        return response
```

##### 中间件的执行顺序 
```text
在视图被处理前(输入)，中间件由上至下依次执行
在视图被处理后(输出)，中间件由下至上依次执行

1. 先按照正序执行每个注册中间件的process_request方法,process_request方法返回的
值是None,就依次执行,如果返回的值是HttpResponse对象，不再执行后面的process_request
方法,而是执行当前对应中间件的process_response方法.
如1-6个中间件,第3个中间件返回HttpResponse对象，接下来执行3、2、1的process_request方法

2. 如果process_request都返回None,则都执行完后，匹配路由，找到要执行的视图函数，先不
执行视图函数,先执行中间件中的process_view方法,process_view方法返回None,继续按顺序执行,
所有的process_view方法执行完后执行视图函数.假如中间件3process_view方法返回了HttpResponse
对象,则4、5、6的process_view和视图函数都不执行, 直接从最后一个中间件,也就是中间件6的
process_response方法开始倒序执行 e
```
















