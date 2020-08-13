# Generated by Django 3.0.6 on 2020-08-09 21:04

import django.contrib.postgres.fields.jsonb
import django.utils.timezone
import django_better_admin_arrayfield.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalisedCrawl",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "start_urls",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=100),
                        size=None,
                    ),
                ),
                (
                    "extract_data",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        default=None, null=True
                    ),
                ),
            ],
            options={"base_manager_name": "objects",},
        ),
        migrations.AddField(
            model_name="crawlsession",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Time at which the session item was created.",
            ),
        ),
        migrations.AddField(
            model_name="crawlsession",
            name="finished_at",
            field=models.DateTimeField(
                default=None,
                help_text="Time at which the crawl session finished.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="crawlsession",
            name="data",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=None, null=True
            ),
        ),
        migrations.AlterField(
            model_name="crawlsession",
            name="unique_id",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name="CrawlSessionItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Time at which the item was created.",
                    ),
                ),
                (
                    "data",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        default=None, null=True
                    ),
                ),
                (
                    "crawl_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="main.CrawlSession",
                    ),
                ),
            ],
            options={"base_manager_name": "objects",},
        ),
    ]