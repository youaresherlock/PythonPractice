#!usr/bin/python
# -*- coding:utf8 -*-
"""
https://api.jinse.com/v6/www/information/list?catelogue_key=tech
"""
import time
import json
import requests


class JinSeSpider(object):

    def __init__(self, page):
        self.base_url = "https://api.jinse.com/v6/www/information/list?catelogue_key=tech"
        self.next_url = "https://api.jinse.com/v6/www/information/list?catelogue_key=tech&limit=23&information_id={}&flag=down&version=9.9.9&_source=www"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }
        self.page = page

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)

        return response.json()

    def parse_data(self, html_str):
        data_list = html_str["list"]

        content_list = []
        for data in data_list:
            item = dict()
            item["id"] = data["id"]
            item['title'] = data["title"]
            item["picture_url"] = data["extra"]["thumbnail_pic"]
            item["topic_url"] = data["extra"]["topic_url"]
            item["author"] = data["extra"]["author"]
            item["author_avatar"] = data["extra"]["author_avatar"]
            item["read_number"] = data["extra"]["read_number"]
            timestamp = data["extra"]["published_at"]
            item["published_time"] = time.strftime("%Y-%m-%d %H:%M", time.localtime(timestamp))
            content_list.append(item)

        return content_list

    def save_data(self, page, content_list):
        with open('tech_{}.json'.format(page), 'w', encoding='utf8') as f:
            content = json.dumps(content_list, ensure_ascii=False, indent=1)
            f.write(content)

    def run(self):
        next_url = self.base_url
        for page in range(self.page):
            json_html = self.send_request(next_url)
            next_url = self.next_url.format(json_html["bottom_id"])
            content_list = self.parse_data(json_html)
            self.save_data(page, content_list)


if __name__ == '__main__':
    spider = JinSeSpider(1)
    spider.run()
