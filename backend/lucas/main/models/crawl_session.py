from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import JSONField


class CrawlSession(models.Model):
    class Meta:
        base_manager_name = "objects"

    unique_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(
        default=timezone.now, help_text="Time at which the session item was created."
    )
    finished_at = models.DateTimeField(
        default=None, null=True, help_text="Time at which the crawl session finished."
    )
    data = JSONField(default=None, null=True)
