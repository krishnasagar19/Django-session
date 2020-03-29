from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from charging_stations.models import ChargingStation


# Unauthenticated view
def all_charging_stations(request, *args, **kwargs):
    context = {
        'charging_stations':
            ChargingStation.objects.all().prefetch_related('charging_point')
    }
    return render(request, 'charging_stations.html', context=context)


# Authenticated view
@login_required
def charging_stations(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {
            'charging_stations':
                ChargingStation.objects.all().prefetch_related('charging_point')
        }
        return render(request, 'charging_stations_logged.html', context=context)
    else:
        return redirect('login/')
