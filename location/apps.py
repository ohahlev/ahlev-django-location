from django.apps import AppConfig
from . import __version__ as VERSION

class LocationConfig(AppConfig):
    name = "location"
    verbose_name = "Location Management %s" % VERSION
    