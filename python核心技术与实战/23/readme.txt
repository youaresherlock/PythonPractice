Python GIL(Global Interpreter Lock全局解释器锁)
Python的线程,封装了底层的操作系统线程,在Linux系统里是Pthread(全称为
POSIX Thread), 而在Windows系统里是Windows Thread. 另外,Python的线程,
也完全受操作系统管理,比如协调何时执行、管理内存资源、管理中断等等

# gil global interpreter lock (ipython)
# python中一个线程对应c语言中的一个线程
# gil使得同一时刻只有一个线程运行在一个CPU上执行字节码，无法将多个线程映射到多个cpu上
# gil会根据执行的字节码行数以及时间片释放GIL，遇到IO操作也会释放

CPython引进GIL其实主要有两个原因:
    1. 为了规避类似于内存管理这样的复杂的竞争风险问题(race condition)
    2. 因为CPython大量使用C语言库,但大部分c语言库都不是原生线程安全的(线程安全
会降低性能和增加复杂度)

绕过GIL:
    1. 使用JPython(Java实现的Python解释器)
    2. 把关键性能代码,放到别的语言(一般是C++)中实现














