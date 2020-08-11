from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from main import views

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="index.html")),
    url(r"^admin/", admin.site.urls),
    url(r"^api/crawl/", views.CrawlView.as_view()),
]
