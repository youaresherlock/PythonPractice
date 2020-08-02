#!usr/bin/python
# -*- coding:utf8 -*-


class Foo:
    def __init__(self):
        print('__init__ called')

    def __enter__(self):
        print('__enter__ called')
        return self

    """
    手动raise异常,顺利捕捉并处理,如果__exit__()没有返回True,异常
    仍然会被抛出
    """
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('__exit__ called')
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_tb}')
            print('exception handled')
        return True


with Foo() as obj:
    raise Exception('exception raised').with_traceback(None)

