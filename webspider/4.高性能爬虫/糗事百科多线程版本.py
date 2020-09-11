#!usr/bin/python
# -*- coding:utf8 -*-
"""
糗事百科段子爬取 多线程版本
https://www.qiushibaike.com/text/page/1/
"""
import time
import requests
import threading
from lxml import etree
from queue import Queue


class QiuBaiSpider(object):

    def __init__(self):
        self.temp_url = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }
        # 准备队列 存储：url 响应内容  数据内容
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    def get_url_list(self):
        """
        准备13页 url地址的方法
        :return: url地址的列表
        """
        for i in range(1, 14):
            # 将生成的url地址放到 url队列中
            self.url_queue.put(self.temp_url.format(i))

    def send_request(self):
        """
        发送请求、获取响应的方法
        :return: 响应内容
        """
        while True:
            # 从Url队列中获取url地址
            url = self.url_queue.get()
            print(f"正在抓取： {url}")
            response = requests.get(url, headers=self.headers)
            # 将响应内容放到 html 队列中
            self.html_queue.put(response.content.decode())
            # url 队列计数 -1
            self.url_queue.task_done()

    def get_content_list(self):
        """
        解析数据的方法
        :return: 数据的列表
        """
        while True:
            # 从html队列中取出html内容
            html_str = self.html_queue.get()
            # 将html_str转换成element对象
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@class='col1 old-style-col1']/div")
            # 保存数据的列表
            content_list = []
            for div in div_list:
                item = dict()
                item["user_name"] = div.xpath(".//h2/text()")[0].strip()
                content_list.append(item)
            # 将输入放入到 content_list_queue
            self.content_list_queue.put(content_list)
            # 将html队列的计数 -1
            self.html_queue.task_done()

    def save_content_list(self):
        """
        保存数据的方法
        :return: 无
        """
        while True:
            # 从content_list_queue中取出数据
            content_list = self.content_list_queue.get()
            for content in content_list:
                print(content)
            # content_list_queue计数-1
            self.content_list_queue.task_done()

    def run(self):
        # 1. 准备url地址
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2. 遍历发送请求，获取响应
        for i in range(3):
            t_parse = threading.Thread(target=self.send_request)
            thread_list.append(t_parse)
        time.sleep(3)
        # 3. 提取数据
        t_content = threading.Thread(target=self.get_content_list)
        thread_list.append(t_content)
        # 4. 保存数据
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        # 启动线程
        for t in thread_list:
            # 把子线程设置为守护线程，当前这个线程不重要，主线程结束，子线程结束
            t.setDaemon(True)
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_list_queue]:
            # 让主线程阻塞，等待队列的计数为0，
            q.join()

        print("主线程结束....")


if __name__ == '__main__':
    spider = QiuBaiSpider()
    spider.run()























