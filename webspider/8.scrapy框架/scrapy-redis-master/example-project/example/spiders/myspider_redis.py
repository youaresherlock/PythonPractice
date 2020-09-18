from scrapy_redis.spiders import RedisSpider


# 分布式的类 继承  RedisSpider
class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    # 爬虫名字
    name = 'myspider_redis'
    # 在分布式的爬虫类中没有start_urls ，但是又一个redis_key  指定起始页的url地址
    # 分布式：统一的调度器存储request对象
    # 程序刚运行起来的时候  没有start_url地址，程序阻塞等待，等待redis_key 中有数据
    redis_key = 'myspider:start_urls'

    # 生成 allowed domains
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
