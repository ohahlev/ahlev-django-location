from django.apps import AppConfig
from django.utils.html import format_html
from . import __version__ as VERSION

class LocationConfig(AppConfig):
    name = 'location'
    verbose_name = format_html("Location Management {}", VERSION)
    