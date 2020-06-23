#!usr/bin/python
# -*- coding:utf8 -*-
"""
python 限制函数执行时间，自己实现 timeout
"""
import time
import signal


# 装饰器工厂
def set_timeout(num, callback):
    def wrap(func):
        # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame
        def handle(signum, frame):
            print(signum, frame)
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                # 设置信号和回调函数
                signal.signal(signal.SIGALRM, handle)
                signal.alarm(num)  # 设置num秒的闹钟
                print("start alarm signal.")
                r = func(*args, **kwargs)
                print("close alarm signal.")
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap


if __name__ == '__main__':
    def after_timeout():
        print("do something after timeout")

    @set_timeout(2, after_timeout)
    def connect():
        time.sleep(1)
        return "connect success."

    print(connect())




























