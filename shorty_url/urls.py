from django.urls import path, re_path, include

from shortener.views import UrlView

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('api/', include('shortener.urls')),
    re_path(r'^(?P<url_hash>.+)$', UrlView.as_view()),
]
