import json
from urllib.parse import urlparse
from uuid import uuid4

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import CrawlSession
from main.scrapyd import get_scrapyd_api


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return False

    return True


class CrawlView(views.APIView):
    permission_classes = [
        AllowAny,
    ]

    @classmethod
    def post(cls, request: Request):
        url = request.data.get("url", None)

        if not url:
            return Response(data="Missing  url", status=400)

        if not is_valid_url(url):
            return Response(data="Invalid  url", status=400)

        scrapyd = get_scrapyd_api()
        domain = urlparse(url).netloc  # parse the url and extract the domain
        unique_id = str(uuid4())
        settings = dict(
            unique_id=unique_id,
            USER_AGENT="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        )
        task_id = scrapyd.schedule(
            "default", "lucas_crawl_spider", settings=settings, url=url, domain=domain
        )

        return Response(dict(taskID=task_id, uniqueID=unique_id), status=200)

    @classmethod
    def get(cls, request: Request):
        task_id = request.GET.get("taskID", None)
        unique_id = request.GET.get("uniqueID", None)

        if not task_id or not unique_id:
            return Response(data="Missing  args", status=400)

        scrapyd = get_scrapyd_api()
        status = scrapyd.job_status("default", task_id)
        if status == "finished":
            session = CrawlSession.objects.filter(unique_id=unique_id).first()

            if not session:
                return Response(dict(crawlResults=[], status=status), status=400)
            return Response(
                dict(crawlResults=json.loads(session.data), status=status), status=200
            )

        return Response(data=dict(status=status))
