from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = [ 'name',  'date_created', 'last_updated', 'latitude', 'longitude', 'address', 'preview_detail' ]
    search_fields = ['name', 'latitude', 'longitude', 'address', 'detail']
    readonly_fields = ['preview']
    fieldsets = [
        ('Location Detail', {
            'fields': ['name', 'address', 'latitude', 'longitude', 'detail']
        }),
        ('Location Preview', {
            'fields': ['preview'],
        }),
    ]
    class Media:
        css = {
        'all': (
            'location/css/location-admin.css',
            )
        }
        js = (
            'location/js/location-admin.js',
        )
    def preview(self, obj):
        return obj.preview()

admin.site.register(Location, LocationAdmin)