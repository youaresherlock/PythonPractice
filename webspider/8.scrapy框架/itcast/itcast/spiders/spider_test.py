from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BaiDuSpider(CrawlSpider):
    name = ""
    allowed_domains = []
    start_urls = []

    rules = (
        Rule(LinkExtractor(), callback="", follow=True),
        Rule(LinkExtractor(), follow=True)
    )

    def parse_item(self, repsonse):
        pass
