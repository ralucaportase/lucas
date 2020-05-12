import scrapy


class LinkItem(scrapy.Item):
    url = scrapy.Field()
