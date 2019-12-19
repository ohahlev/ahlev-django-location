from django.shortcuts import render, get_list_or_404
from .models import Location

def index(request):
    locations = get_list_or_404(Location)
    context = {
        'location': locations[0],
    }
    return render(request, 'location/index.html', context=context)