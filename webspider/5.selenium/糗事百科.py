#!usr/bin/python
# -*- coding:utf8 -*-
import time
from selenium import webdriver


class QiuBaiSpider(object):

    def __init__(self):
        self.url = 'https://www.qiushibaike.com/text/page/1/'
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def parse_data(self):
        # 对数据进行分组
        div_list = self.driver.find_elements_by_xpath("//div[@class='col1 old-style-col1']/div")
        content_list = []
        for div in div_list:
            item = dict()
            item['username'] = div.find_element_by_xpath('.//h2').text
            item['content'] = div.find_element_by_xpath('.//div[@class="content"]/span').text
            print(item)

            content_list.append(item)

        return content_list

    def save_data(self, content_list):
        for content in content_list:
            print(content)

    def run(self):
        self.driver.get(self.url)
        content_list = self.parse_data()
        self.save_data(content_list)
        while True:
            next_url = self.driver.find_elements_by_xpath('//span[@class="next"]')
            if len(next_url) > 0:
                next_url[0].click()

                content_list = self.parse_data()
                self.save_data(content_list)
            else:
                break


if __name__ == '__main__':
    spider = QiuBaiSpider()
    spider.run()






















