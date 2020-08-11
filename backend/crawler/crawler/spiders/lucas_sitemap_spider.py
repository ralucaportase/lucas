from scrapy.spiders import SitemapSpider


class LucasSitemapSpider(SitemapSpider):
    name = "lucas_sitemap_spider"
    handle_httpstatus_list = [403, 404, 500]

    def __init__(self, *args, **kwargs):
        self.sitemap_urls = kwargs.get("sitemap_urls")
        self.sitemap_follow = kwargs.get("sitemap_follow")

    def parse(self, response):
        return dict(address=response.url)
