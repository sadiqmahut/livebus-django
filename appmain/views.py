
from django.shortcuts import render
from django.http import JsonResponse
from .models import BStop, Route, Stops, Buses
import json
from django.core.serializers import serialize

# Create your views here.
'''
ADMIN VIEW
'''

def send_stops(request, route):
    bus = Buses.objects.filter(broute = route).values()
    data = dict(d=list(Stops.objects.filter(sroute = route).values()),b=list(bus))

    return JsonResponse(data)

def update_stops(request, route, stop):
    try:
        bus = Buses.objects.get(broute = route)
        bus.b_cur_stop = stop
        bus.save()
    except:
        pass

def homepage_admin(request):
    context = {}
    routes = Route.objects.all()
    context['routes'] = routes
    return render(request, 'base.html', context)


    
def index_page(request):
    context = {}
    buses = Buses.objects.all()
    context['buses'] = buses
    return render(request, 'client.html',context)

def buspage(request, pk):
    context = {}
    bus = Buses.objects.get(pk = pk)
    context['bus'] = bus
    return render(request, 'bus.html', context)