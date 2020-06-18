from main.models import CrawlSession
import json


class LucasCrawlerPipeline:
    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.links = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(unique_id=crawler.settings.get("unique_id"),)

    def close_spider(self, spider):
        session = CrawlSession()
        session.unique_id = self.unique_id
        session.data = json.dumps(self.links)
        session.save()

    def process_item(self, item, spider):
        self.links.append(dict(address=item.get("address")))

        return item
