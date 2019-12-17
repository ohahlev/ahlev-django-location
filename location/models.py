from django.db import models
from django.utils.text import Truncator
from django.utils.html import format_html

class Location(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    detail = models.TextField(max_length=1025)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Location'
    
    def __str__(self):
        return self.name

    def short_detail(self):
        return Truncator(self.detail).chars(30)

    short_detail.admin_order_field = 'detail'
    short_detail.short_description = 'detail'