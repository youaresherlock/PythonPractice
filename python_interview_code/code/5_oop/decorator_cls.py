#!usr/bin/python
# -*- coding:utf8 -*-
# 用类编写装饰器
import time

class LogTime:

    def __init__(self, use_int=False):
        self.use_int = use_int

    def __call__(self, func):
        def _log(*args, **kwargs):
            beg = time.time()
            res = func(*args, **kwargs)
            if self.use_int:
                used_time = int(time.time() - beg)
            else:
                used_time = (time.time()-beg)
            print('use time: {}'.format(used_time))
            return res

        return _log

@LogTime(use_int=False)
def mysleep():
    time.sleep(1)

if __name__ == '__main__':
    mysleep()
























