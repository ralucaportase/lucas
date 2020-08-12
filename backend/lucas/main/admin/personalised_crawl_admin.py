from uuid import uuid4

from django import forms
from django.contrib import admin
from django.contrib.postgres import fields
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.template.loader import render_to_string
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_json_widget.widgets import JSONEditorWidget

from main.scrapyd import get_scrapyd_api


def validate_urls(urls):
    url_validator = URLValidator()
    wrong_urls = []
    for url in urls:
        try:
            url_validator(url)
        except ValidationError:
            wrong_urls.append(url)

    if len(wrong_urls) > 0:
        raise ValidationError({"start_urls": f"Invalid urls:{wrong_urls}"})


class PersonalisedCrawlAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonalisedCrawlAdminForm, self).__init__(*args, **kwargs)
        self.fields["extract_data"].help_text = render_to_string("personalised_crawl_help_text.html")

    def clean(self):
        cleaned_data = super().clean()

        start_urls = cleaned_data.get("start_urls")
        validate_urls(start_urls)

        return cleaned_data


class PersonalisedCrawlAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        fields.JSONField: {"widget": JSONEditorWidget},
    }
    list_display = ("name",)

    form = PersonalisedCrawlAdminForm

    # Every time we open a PersonalisedCrawl this will execute
    # This is temporary
    def view_on_site(self, personalised_crawl):
        scrapyd = get_scrapyd_api()
        unique_id = str(uuid4())
        settings = dict(
            unique_id=unique_id,
            USER_AGENT="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        )
        scrapyd.schedule(
            "default",
            "lucas_personalised_crawl_spider",
            settings=settings,
            personalised_crawl_id=personalised_crawl.id,
        )
        return "/admin/main/crawlsession/"
