from scrapy.spiders import CrawlSpider, Rule


class LucasCrawlSpider(CrawlSpider):
    name = "lucas_crawl_spider"
    handle_httpstatus_list = [403, 404, 500]

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get("url")
        self.domain = kwargs.get("domain")
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        LucasCrawlSpider.rules = [
            Rule(callback="parse_item", follow=True),
        ]
        super(LucasCrawlSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        return dict(address=response.url)
