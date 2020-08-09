from django.contrib import admin
from main.models import PersonalisedCrawl, CrawlSession
from .personalised_crawl_admin import PersonalisedCrawlAdmin
from .crawl_session_admin import CrawlSessionAdmin

admin.site.register(CrawlSession, CrawlSessionAdmin)
admin.site.register(PersonalisedCrawl, PersonalisedCrawlAdmin)
