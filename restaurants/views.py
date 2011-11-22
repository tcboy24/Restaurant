from django.shortcuts import render_to_response
from restaurants.models import Restaurants


def homepage(request):
    rests = Restaurants.objects.order_by('name')
    return render_to_response('homepage.html', {
        'rests': rests,
    })

def detail(request, restaurants_id):
    rests = Restaurants.objects.get(id=restaurants_id)
    return render_to_response('detail.html', {
        'rests': rests,
    })


