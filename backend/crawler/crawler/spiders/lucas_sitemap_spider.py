from scrapy.spiders import SitemapSpider


class LucasSitemapSpider(SitemapSpider):
    name = "lucas_sitemap_spider"
    sitemap_urls = ["https://baan.kaidee.com/sitemap.xml"]
    sitemap_follow = ["/categories"]

    def parse(self, response):
        return dict(address=response.url)
