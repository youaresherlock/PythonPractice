#!/usr/bin/python
# -*- coding:utf8 -*-

'''
初始化新闻数据
'''
from datetime import datetime
from redis_news import RedisNews


list_news = [
    {
        "title": "朝鲜特种部队视频公布 展示士兵身体素质与意志",
        "img_url": "/static/img/news/01.png",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "推荐",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "男子长得像\"祁同伟\"挨打 打人者:为何加害检察官",
        "img_url": "/static/img/news/02.png",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "百家",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "导弹来袭怎么办？日本政府呼吁国民躲入地下通道",
        "img_url": "/static/img/news/03.png",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "本地",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "美媒:朝在建能发射3发以上导弹的3000吨级新潜艇",
        "img_url": "/static/img/news/04.png",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "推荐",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "证监会:前发审委员冯小树违法买卖股票被罚4.99亿",
        "img_url": "/static/img/news/08.png",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "百家",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "外交部回应安倍参拜靖国神社:同军国主义划清界限",
        "img_url": "/static/img/news/new1.jpg",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "推荐",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "外交部回应安倍参拜靖国神社:同军国主义划清界限",
        "img_url": "/static/img/news/new1.jpg",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "百家",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "title": "\"萨德\"供地违法？韩民众联名起诉要求撤回供地",
        "img_url": "/static/img/news/new1.jpg",
        "content": "新闻内容",
        "is_valid": 1,
        "news_type": "百家",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
]

def main():
    ''' 初始化新闻数据 '''
    redis_news = RedisNews()
    redis_news.init_news(list_news)
    # news_list = redis_news.get_all_news()
    # print(news_list)

if __name__ == '__main__':
    main()

