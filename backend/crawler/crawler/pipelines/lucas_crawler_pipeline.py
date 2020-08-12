from django.utils import timezone

from main.models import CrawlSession, CrawlSessionItem


class LucasCrawlerPipeline:
    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.crawl_session = CrawlSession(unique_id=unique_id)
        self.crawl_session.save()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(unique_id=crawler.settings.get("unique_id"))

    def close_spider(self, spider):
        crawl_session_data = list(self.crawl_session.items.values_list("data", flat=True))
        self.crawl_session.data = crawl_session_data
        self.crawl_session.finished_at = timezone.now()
        self.crawl_session.save()

    def process_item(self, item, spider):
        crawl_session_item = CrawlSessionItem(crawl_session=self.crawl_session, data=item)
        crawl_session_item.save()
        return item
