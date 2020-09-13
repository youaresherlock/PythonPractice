#!usr/bin/python
# -*- coding:utf8 -*-
"""
url http://fanyi.youdao.com/

i: 你好
from: zh-CHS
to: en
smartresult: dict
client: fanyideskweb


salt: 15999010448871
sign: 69a52a3010eba1cca3d4f9a3c10d5cc1
lts: 1599901044887
bv: 02edb5d6c6ac4286cd4393133e5aab14
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
"""
import time
import random
import hashlib
import requests


class YouDaoSpider(object):

    def __init__(self, word):
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Cookie": "OUTFOX_SEARCH_USER_ID=2004598202@10.108.160.19; JSESSIONID=aaaI4kXrPNu8RaSc3pFjx; OUTFOX_SEARCH_USER_ID_NCOO=111942816.21549504; ___rl__test__cookies=1590736092492",
            "Referer": "http://fanyi.youdao.com/"
        }
        self.formdata = {}
        self.word = word

    def generate_formdata(self):
        """
            ts: r = "" + (new Date).getTime()
            bv: t
            salt: i =  r + parseInt(10 * Math.random(), 10);
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        :return:
        """
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))

        temp_str = "fanyideskweb" + self.word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        md5 = hashlib.md5()
        # bytes类型
        md5.update(temp_str.encode())
        sign = md5.hexdigest()

        self.formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "b286f0a34340b928819a6f64492585e8",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }

    def send_request(self):
        response = requests.post(self.url, headers=self.headers, data=self.formdata)
        return response.json()

    def parse_data(self, data):
        result = data["translateResult"][0][0]["tgt"]
        print(f"{self.word} 的翻译结果是：{result}")

    def run(self):
        # 生成 formdata
        self.generate_formdata()
        # 发送请求 获取响应
        data = self.send_request()
        self.parse_data(data)


if __name__ == '__main__':
    youdao = YouDaoSpider("面条")
    youdao.run()















