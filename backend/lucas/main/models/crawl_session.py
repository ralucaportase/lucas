from django.db import models


class CrawlSession(models.Model):
    class Meta:
        base_manager_name = "objects"

    unique_id = models.CharField(max_length=255)
    data = models.TextField(default=None, null=True)
