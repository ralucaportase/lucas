from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class CrawlSessionItem(models.Model):
    class Meta:
        base_manager_name = "objects"

    crawl_session = models.ForeignKey(
        "CrawlSession", on_delete=models.CASCADE, related_name="items"
    )

    created_at = models.DateTimeField(
        default=timezone.now, help_text="Time at which the item was created."
    )
    data = JSONField(default=None, null=True)
