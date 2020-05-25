from scrapyd_api import ScrapydAPI

from lucas import settings


def get_scrapyd_api():
    return ScrapydAPI(settings.SCRAPPYD_URL)
