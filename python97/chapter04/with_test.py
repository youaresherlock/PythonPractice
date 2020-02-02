#!usr/bin/python
# -*- coding:utf8 -*-

# try except finally
def exe_try():
    try:
        f_read = open("bobby.txt")
        print("code started")
        raise KeyError
    except KeyError as e:
        print("key error")
    except IndexError as e:
        print("index error")
    # 没有抛出异常的时候运行
    else:
        print("other error")
    # 无论与否都会运行这里代码
    finally:
        print("finally")

# with语句简化try...finally
# 上下文管理器 __enter__  __exit__
class Sample():
    def __enter__(self):
        print("enter")
        # 获取资源
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")
    def do_something(self):
        print("do something")

with Sample() as sample:
    sample.do_something()

# if __name__ == "__main__":
#     result = exe_try()
#     print(result)






















