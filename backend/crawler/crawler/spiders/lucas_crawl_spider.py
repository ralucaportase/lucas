from scrapy.spiders import CrawlSpider, Rule

from crawler.items import LinkItem


class LucasCrawlSpider(CrawlSpider):
    name = 'lucas_crawl_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    rules = (
        Rule(callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        return LinkItem(url=response.url)
