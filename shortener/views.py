from django.shortcuts import get_object_or_404, redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from ipware import get_client_ip

from .models import URL, Visitor


class UrlShortener(APIView):
    def post(self, request, origin_uri):
        try:
            url = URL.objects.get(full_url=origin_uri)
        except URL.DoesNotExist:
            ip = get_client_ip(request)
            url = URL(full_url=origin_uri, created_by=ip)
            url.save()

        short_url = url.short_url

        return Response({"short_url": short_url})


class UrlView(APIView):
    def get(self, request, url_hash):
        url = get_object_or_404(URL, url_hash=url_hash)
        url.clicked()
        url.last_visit()
        visitor = Visitor()
        visitor.visitor = get_client_ip(request)
        visitor.url_id = url.id
        visitor.save()
        url.save()
        go_to_url = url.full_url

        return redirect(go_to_url)


class UrlStatistics(APIView):
    def get(self, request, url_hash):
        url = URL.objects.get(url_hash=url_hash)
        if str(url.created_by) == str(get_client_ip(request)):
            short_url = url.short_url
            clicks = url.clicks
            last_visited = url.last_visited

            response = {"short_url": short_url,
                        "clicks": clicks,
                        "last_visited": last_visited}
            return Response(response)
        else:
            return Response('Wrong link')


class DeleteUrl(APIView):
    def delete(self, request, url_hash):
        url = get_object_or_404(URL, url_hash=url_hash)
        if str(url.created_by) == str(get_client_ip(request)):
            url.delete()
            return Response({"message": "Url `{}` has been deleted.".format(url.short_url)}, status=200)
        else:
            return Response('Wrong link')
