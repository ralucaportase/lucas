import os
import sys
import django

# DJANGO INTEGRATION

DJANGO_PROJECT_NAME = "lucas"
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(".")), DJANGO_PROJECT_NAME)
)
os.environ["DJANGO_SETTINGS_MODULE"] = "lucas.settings"

django.setup()

# DJANGO INTEGRATION

BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "crawler.pipelines.LucasCrawlerPipeline": 300,
}
