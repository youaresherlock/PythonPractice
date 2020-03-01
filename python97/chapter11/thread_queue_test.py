#!usr/bin/python
# -*- coding:utf8 -*-

# 通过queue的方式进行线程间的同步
from queue import Queue

import time
import threading

detail_url_list = []

def get_detail_html(queue):
    # 爬取文章详情页
    while True:
            url = queue.get()
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")

def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(2)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

# 1.线程间通信-共享变量

if __name__ == "__main__":
    detail_url_list = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
























