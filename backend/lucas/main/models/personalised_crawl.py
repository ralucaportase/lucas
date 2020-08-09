from django.db import models
from django.contrib.postgres.fields import JSONField
from django_better_admin_arrayfield.models.fields import ArrayField


class PersonalisedCrawl(models.Model):
    class Meta:
        base_manager_name = "objects"

    name = models.CharField(max_length=255)
    start_urls = ArrayField(models.CharField(max_length=100, blank=True))
    extract_data = JSONField(default=None, null=True)
