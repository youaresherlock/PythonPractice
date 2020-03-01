#!usr/bin/python
# -*- coding:utf8 -*-

# 对于io操作来说，多线程和多进程性能差别不大
# 1.通过Thread类实例化
import time
import threading
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     start_time = time.time()
#     """
#     设置子线程为守护线程，主线程执行完后子线程会自动kill掉
#     thread1.setDaemon(True)
#     thread2.setDaemon(True)
#     """
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#     # 主线程和子线程默认是非守护线程，主线程退出之后子线程还会继续执行
#     print("last time: {}".format(time.time() - start_time))


# 2.通过继承Thread来实现多线程

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end")

if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    # 主线程和子线程默认是非守护线程，主线程退出之后子线程还会继续执行
    print("last time: {}".format(time.time() - start_time))





































