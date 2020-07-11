from django.urls import re_path

from .views import UrlShortener, UrlStatistics, DeleteUrl


app_name = "shortener"

urlpatterns = [
    re_path(r'^shortener/(?P<origin_uri>.+)$', UrlShortener.as_view()),
    re_path(r'^statistics/(?P<url_hash>.+)$', UrlStatistics.as_view()),
    re_path(r'^delete/(?P<url_hash>.+)$', DeleteUrl.as_view()),
]
