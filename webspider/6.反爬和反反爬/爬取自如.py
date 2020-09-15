#!usr/bin/python
# -*- coding:utf8 -*-
import re
import pytesseract
import requests
from PIL import Image
from lxml import etree
from pprint import pprint


class ZiroomSpider(object):

    def __init__(self):
        self.url = "http://www.ziroom.com/z/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }

    def send_request(self, url):
        """
        发送请求 获取相应的方法
        :param url: 要发送请求的url地址
        :return: 响应内容
        """
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_price(self, price_img_url, price_list):
        """
        获取真实的价格信息
        :param price_img_url: 价格图片的url地址
        :param price_list: 图片偏移量的列表
        :return: 真实的价格
        """
        # 发送图片的url地址请求
        image_content = self.send_request(price_img_url)
        # 保存图片
        with open("num.png", "wb") as f:
            f.write(image_content)
        image = Image.open("num.png")
        # # 获取图片的尺寸大小
        x, y = image.size
        try:
            # 将图片的透明背景 变成白色的，增加识别度
            p = Image.new("RGBA", image.size, (255, 255, 255))
            p.paste(image, (0, 0, x, y), image)
            p.save("num.png")
        except:
            pass
        # 对图片中的内容进行识别
        code = pytesseract.image_to_string(image, lang="eng", config="--psm 6")

        num = 21.4
        real_price = ""

        for price in price_list:
            # 获取数据对应的下标
            res = int(float(price) / num)
            # 根据下标取出来对应真是的数字数据，并进行拼接真实的价格
            real_price += code[res]

        return real_price

    def parse_data(self, html_str):
        """
        解析数据的方法
        :param html_str: 响应源码
        :return: 数据列表
        """
        # print(html_str)
        html = etree.HTML(html_str)
        # 对数据进行分组
        div_list = html.xpath("//div[@class='Z_list-box']/div")
        content_list = []
        for div in div_list[:3]:
            item = {}
            img_url = div.xpath("./div[@class='pic-box']/a/img/@src")[0]
            if img_url is not None:
                item["image_url"] = "http:" + img_url
            else:
                continue
            item["title"] = div.xpath(".//h5/a/text()")[0]
            item["desc"] = div.xpath(".//div[@class='desc']/div/text()")[0]
            item["location"] = div.xpath(".//div[@class='location']/text()")[0].strip()

            # 获取价格列表
            price_list = str(div.xpath(".//div[@class='price ']//span/@style|.//div[@class='price red']//span/@style"))
            print(price_list)
            # 获取价格图的url地址  http://static8.ziroom.com/phoenix/pc/images/price/new-list/a8a37e8b760bc3538c37b93d60043cfc.png
            price_img_url = "http:" + re.findall(r"background-image: url\((.*?)\);", price_list)[0]
            print(price_img_url)
            # 获取图片具体 数字的位置
            price_list = re.findall(";background-position: -(.*?)px", price_list)
            # 调用方法获取 真实的价格信息
            room_price = self.get_price(price_img_url, price_list)
            item["room_price"] = room_price
            item["tag"] = div.xpath(".//div[@class='tag']//span/text()")[0]
            content_list.append(item)

        return content_list

    def save_data(self, content_list):
        """
        保存数据的方法
        :param content_list: 要保存的数据列表
        :return:
        """
        for content in content_list:
            pprint(content)

    def run(self):
        # 1. 准备url地址
        # 2. 发送请求 获取响应
        html = self.send_request(self.url)
        # 3. 解析数据
        content_list = self.parse_data(html)
        # 4. 保存数据
        self.save_data(content_list)


if __name__ == '__main__':
    ziroom = ZiroomSpider()
    ziroom.run()