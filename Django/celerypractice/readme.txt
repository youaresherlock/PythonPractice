celery:
    分布式任务队列,架构是比较典型的生产者消费者模型. 发布任务的客户端是生产者,
每一个消费者有一个主进程负责调度任务,同时有一个或多个子进程负责执行任务.
client和worker之间的消息传递通过broker, celery的broker依赖于第三方的消息
队列,如redis,rabbitMQ等.
Celery的架构:
    由三部分组成,消息中间件(message broker),任务执行单元(worker)和任务执行结果
存储(task result store)组成
choose a broker:
    rabbitmq、redis

celery的工作模式:

协程模式:
celery -A tasks worker -l info -P eventlet -E

celery -A celery_tasks.main worker -l info -P eventlet -c 1000