什么是Restful
    Representational State Transfer
    HTTP协议(1.0/1.1)的主要设计者Roy Thomas Fielding提出
    资源Resources 表现层Representation 状态转化State Transfer

Restful解释:
    Resources(资源): 使用URI指向的一个实体
    Representation(表现层): 资源的表现形式，比如图片、HTML文本等
    State Transfer(状态转换): GET、POST、PUT、DELETE HTTP动词来操作资源

GET/POST/PUT/DELETE 分别用来 获取/新建/更新/删除 资源
幂等性: GET/PUT/DELETE是幂等操作
幂等指的是无论一次还是多次操作具有一样的副作用

Tornado Restful Api示例
GET http://[hostname]/api/users 检索用户列表
GET http://[hostname]/api/users/[user_id] 检索单个用户
POST http://[hostname]/api/users 创建新用户
PUT http://[hostname]/api/users/[user_id] 更新用户信息
DELET http://[hostname]/api/users/[user_id] 删除用户

Tornado进阶
用Tornado实现异步网络服务
Tornado使用Peewee, Motor等连接MYSQL, Mongodb数据库
引入表单验证、用户认证等模块




















































