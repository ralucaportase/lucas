from django.conf.urls import url

from main import views


urlpatterns = [
    url(r"^api/crawl/", views.CrawlView.as_view()),
]
