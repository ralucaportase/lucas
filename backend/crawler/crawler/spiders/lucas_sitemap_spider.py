from scrapy.spiders import SitemapSpider

from crawler.items import LinkItem


class LucasSitemapSpider(SitemapSpider):
    name = 'lucas_sitemap_spider'
    sitemap_urls = ['https://baan.kaidee.com/sitemap.xml']
    sitemap_follow = ['/categories']

    def parse(self, response):
        return LinkItem(url=response.url)
