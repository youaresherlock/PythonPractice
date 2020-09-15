#!usr/bin/python
# -*- coding:utf8 -*-
"""
url https://www.qidian.com/all?chanId=21&subCateId=8
"""
import re
import json
import requests
from lxml import etree
from fontTools.ttLib import TTFont, BytesIO


class QiDianSpider(object):

    def __init__(self):
        self.url = "https://www.qidian.com/all?chanId=21&subCateId=8"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }
        # 通过字体编辑器 打开的字体文件中的映射关系
        self.woff_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "zero": "10",
            "period": ".",
        }

    def send_request(self, url):
        """
        发送请求，获取响应的方法
        :param url: 发送请求的url地址
        :return: 响应内容
        """
        response = requests.get(self.url, headers=self.headers)
        with open("a.html", 'w', encoding="utf-8") as f:
            f.write(response.content.decode())
        return response.content

    def get_words_num(self, response):
        """
        获取正确的字数的对应字体映射关系字典
        :param response: 当前页面的响应内容
        :return:
        """
        # 将网页内容转换 成 element对象，
        html = etree.HTML(response)
        # 获取字体样式内容
        style = html.xpath("//p[@class='update']/span/style/text()")[0]
        # 使用正则表达式 获取 字体的url地址
        font_url = re.findall(r"format\('eot'\); src: url\('(.*?)'\) format\('woff'\)", style)[0]
        # 根据url地址  获取字体的响应内容
        woff = requests.get(font_url, headers=self.headers)
        # 将字体文件的响应内容转成内存文件 交给TTfont处理
        font = TTFont(BytesIO(woff.content))
        # 获取字体映射关系
        font_map = font.getBestCmap()
        print(font_map)
        for key in font_map.keys():
            # 根据 font_map中的 key 对应的值 替换成对应的真实的数字
            font_map[key] = self.woff_map[font_map[key]]
        print(font_map)
        for key in font_map.keys():
            value = font_map.pop(key)
            # 将 font_map 键值对转换成和页面抓取下来的内容一样的格式的 对应关系  {"&#100117;": 3}
            font_map["&#" + str(key) + ";"] = value

        # 将 响应源码中的字体内容，转换成真是的数据
        html_str = response.decode()
        for key, value in font_map.items():
            if key in html_str:
                html_str = html_str.replace(key, value)

        with open("qidian1.html", "w", encoding="utf-8") as f:
            f.write(html_str)

        return html_str

    def parse_data(self, html_str):
        """
        数据解析的方法
        :param html_str: 替换后的html 源码
        :return: 数据列表
        """
        html = etree.HTML(html_str)
        # 对数据进行分组
        # 获取小说的列表
        li_list = html.xpath("//ul[@class='all-img-list cf']/li")

        content_list = []
        for li in li_list:
            item = dict()
            # 获取图书的名字
            item["book_name"] = li.xpath(".//h4/a/text()")[0]
            # 获取图书的图片链接
            item["book_img_href"] = "https:" + li.xpath("./div[@class='book-img-box']//img/@src")[0]
            # 获取图书的作者
            item["book_author"] = li.xpath(".//a[@class='name']/text()")[0]
            # 获取图书的额状态
            item["book_status"] = li.xpath(".//p[@class='author']/span/text()")[0]
            # 获取图书的描述信息
            item["book_desc"] = li.xpath(".//p[@class='intro']/text()")[0].strip()
            # 获取图书的字数
            item["fonts_num"] = li.xpath(".//p[@class='update']/span/span/text()")[0] + "万字"

            content_list.append(item)
        return content_list

    def save_data(self, content_list):
        """
        保存数据的方法
        :param content_list: 数据列表
        :return:
        """
        with open('qidian.json', 'w', encoding='utf8') as f:
            content = json.dumps(content_list, ensure_ascii=False, indent=1)
            f.write(content)
        for content in content_list:
            print(content)

    def run(self):
        # 1. url
        # 2. 发送请求获取响应
        response = self.send_request(self.url)
        # 3. 获取正确的文字数
        html_str = self.get_words_num(response)
        # 4. 解析数据
        content_list = self.parse_data(html_str)
        # 数据保存
        self.save_data(content_list)


if __name__ == '__main__':
    qidian = QiDianSpider()
    qidian.run()
