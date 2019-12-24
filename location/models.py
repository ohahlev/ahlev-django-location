from django.db import models
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError(
            _('%(value)s is not a valid latitude; it must be between -90 and 90.'),
            params={'value': value},
        )

def validate_longitude(value):
    if value < -180 or value > 180:
        raise ValidationError(
            _('%(value)s is not a valid longitude; it must be between -180 and 180.'),
            params={'value': value},
    )

class Location(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    address = models.CharField(max_length=32, unique=True, blank=False)
    latitude = models.FloatField(blank=False, validators=[validate_latitude])
    longitude = models.FloatField(blank=False, validators=[validate_longitude])
    detail = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Location'
    
    def __str__(self):
        return self.name

    def preview_detail(self):
        return format_html(self.detail)

    preview_detail.admin_order_field = 'detail'
    preview_detail.short_description = 'detail'

    def preview(self):
        return format_html('''
        
        <script async defer src='https://maps.googleapis.com/maps/api/js?key=AIzaSyDbr6x5lbYq7WTHCdzY3f8VLGzoIGLXfJM&callback=init_map'></script>
        <div id='ahlev-map'></div>
        ''')
