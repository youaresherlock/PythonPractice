装饰器的意义:
Decorators is to modify the behavior of the function through
a wrapper so we don't have to actually modify the function.

多线程和多进程的应用场景:
    CPU密集型任务: 多进程
    I/O密集型任务, 优先使用多线程或Asyncio
    I/O操作非常多,非常heavy,需要建立的连接也比较多时,一般选择Asyncio

线程的使用场景?
    线程擅长磁盘I/O
    FastDFS选择线程同步主从
    MYSQL主从同步也是线程实现





































