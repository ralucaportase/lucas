from scrapy.spiders import Spider

from main.models import PersonalisedCrawl


class LucasPersonalisedCrawlSpider(Spider):
    name = "lucas_personalised_crawl_spider"
    handle_httpstatus_list = [403, 404]

    def __init__(self, *args, **kwargs):
        personalised_crawl_id = kwargs.get("personalised_crawl_id")
        self.personalised_crawl = PersonalisedCrawl.objects.get(
            pk=personalised_crawl_id
        )
        self.start_urls = self.personalised_crawl.start_urls
        self.extract_data = self.personalised_crawl.extract_data

        super(LucasPersonalisedCrawlSpider, self).__init__(*args, **kwargs)

    @staticmethod
    def extract_data_from_selector(selector, data_to_extract):
        data = {}
        for key, value in data_to_extract.items():
            if isinstance(value, str):
                data[key] = selector.xpath(value).get()
            else:
                if value.get("type") == "list":
                    data[key] = selector.xpath(value.get("selector")).getall()
        return data

    def parse(self, response):
        for rule in self.extract_data:
            if rule.get("type") == "object":
                yield self.extract_data_from_selector(response, rule.get("data"))
            elif rule.get("type") == "objects":
                for data_selector in response.xpath(rule.get("selector")):
                    yield self.extract_data_from_selector(
                        data_selector, rule.get("data")
                    )
