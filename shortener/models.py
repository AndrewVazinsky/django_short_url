from django.db import models

from hashlib import md5
from datetime import datetime


HOST_NAME = 'http://127.0.0.1:8000/'


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True, db_index=True)
    short_url = models.URLField(unique=True, blank=True, null=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.GenericIPAddressField()
    last_visited = models.DateTimeField(null=True)

    def clicked(self):
        self.clicks += 1
        super().save()

    def last_visit(self):
        self.last_visited = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        super().save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:6]
            self.short_url = self.create_short_url()
        else:
            return self.short_url
        return super().save(*args, **kwargs)

    def create_short_url(self):
        return HOST_NAME + self.url_hash


class Visitor(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    visitor = models.GenericIPAddressField()
