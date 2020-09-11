#!usr/bin/python
# -*- coding:utf8 -*-
"""
获取贴吧的每个标题以及图片
1. 确定url地址 url: https://tieba.baidu.com/f?kw={}

2. 确定抓取的数据的位置 抓取数据的时候 先对数据进行分组 遍历提取数据
分组拿到li列表  //li[@class='']

3. 从列表页中进入到详情页中 对详情页的url地址发送请求
提取图片 //img[@class='BDE_Image']
"""
import os
import time
import requests
from lxml import etree


class TieBaSpider(object):

    def __init__(self, tieba_name):
        self.base_url = "https://tieba.baidu.com"
        self.url = "https://tieba.baidu.com/f?kw={}".format(tieba_name)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Cookie": "PSTM=1581365228; BAIDUID=3644A85DAC42BBB9D49B78CB999BDBDA:FG=1; BIDUPSID=23331049D3B6C931A2E04F70C91AC15B; TIEBAUID=7a2a671ad97a48c0e6f48183; TIEBA_USERTYPE=cb23caaea5fd4553394a57a2; bdshare_firstime=1582296754543; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=6; st_key_id=17; wise_device=0; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1599792011; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1599795881; H_PS_PSSID=7541_32606_1431_7609_7619_32117_7565_26350_32582_22158; tb_as_data=4f03af187ff62bb5c1209dd43c7a8fd50c8bfda25da2fffb93a1502609efa138e73eb833b8433329ca7f0cbf7c9027bf45facd016d37ec10cea8b9797a2430fead7797caa21023dd6980176d0fe2451fb8ef0051b54d543878582454e29ed6a6; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1599806202,1599806204,1599806235,1599806237; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1599806237; st_data=34cb83fc30e8e65d1c18ff7ebb7fd5240e1e70238cad783224d9593581c0385a8d7758e7ab494440822d3bab23498a6caae16ad32fff7d07769c7973216b5275cad6a303a7d0acf8ed7ace3471a59d8bcb143e6355558f5d57d6cde820634b8d5bf69b3774b5099556d230340ce285e3cd66d0911ca78c270fcb1996de6afc00; st_sign=8cdc2752"
        }

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_data(self, response):
        html = response.decode().replace("<!--", "").replace("-->", "")
        element = etree.HTML(html)
        li_list = element.xpath("//ul[@id='thread_list']/li")[1:]
        content_list = []
        for li in li_list[:2]:
            item = {}
            item["title"] = li.xpath(".//a[@class='j_th_tit ']/text()")[0]
            item["href"] = self.base_url + li.xpath(".//a[@class='j_th_tit ']/@href")[0]
            # 发送详情页的请求
            item["img_url_list"] = self.parse_detail(item["href"])
            content_list.append(item)

        next_url = 'https:' + element.xpath(".//a[@class='next pagination-item ']/@href")[0] if len(element.xpath(".//a[@class='next pagination-item ']/@href")) > 0 else None

        return content_list, next_url

    def parse_detail(self, detail_url):
        response = self.send_request(detail_url)
        html = etree.HTML(response)
        img_url_list = html.xpath("//img[@class='BDE_Image']/@src")
        return img_url_list

    def save_content_list(self, content_list):
        print(content_list)
        # 第一部分保存文本
        # content_json = json.dumps(content_list, ensure_ascii=False)
        # if not os.path.exists('tieba_data'):
        #     os.mkdir('tieba_data')
        #
        # with open('tieba_data/' + 'tieba_json.json', 'w') as f:
        #     f.write(content_json)


        # 第二部保存每个帖子里面的图片到本地
        # for content in content_list:
            # id_name = content.get('href').split('/')[-1]
            # if not os.path.exists('tieba_data/' + id_name):
            #     os.mkdir('tieba_data/' + id_name)
            # for img_url in content.get('img_url_list'):
            #     response = requests.get(img_url)
            #     img_name = img_url.split('/')[-1]
            #     with open('tieba_data/' + id_name + '/' + img_name, 'wb') as f:
            #         f.write(response.content)

    def run(self):

        next_url = self.url
        while True:
            time.sleep(3)
            if next_url is None:
                print('获取数据完毕')
                break
            print("=======" + next_url)
            response = self.send_request(next_url)
            content_list, next_url = self.parse_data(response)
            self.save_content_list(content_list)


if __name__ == '__main__':
    spider = TieBaSpider('一拳超人')
    spider.run()























