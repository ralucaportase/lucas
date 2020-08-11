from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

from main.models import CrawlSessionItem


class CrawlSessionItemModelInline(StackedInline):
    formfield_overrides = {
        fields.JSONField: {"widget": JSONEditorWidget},
    }
    model = CrawlSessionItem
    extra = 0
    max_num = 5

    ordering = ("-pk",)
    readonly_fields = ("created_at",)


class CrawlSessionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {"widget": JSONEditorWidget},
    }

    inlines = [
        CrawlSessionItemModelInline,
    ]
    list_display = ("unique_id", "created_at", "finished_at")
    readonly_fields = ("unique_id", "created_at", "finished_at")
