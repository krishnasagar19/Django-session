from django.shortcuts import render

from charging_stations.models import ChargingStation


# Unauthenticated view
def all_charging_stations(request, *args, **kwargs):
    context = {
        'charging_stations':
            ChargingStation.objects.all().prefetch_related('charging_point')
    }
    return render(request, 'charging_stations.html', context=context)


# Authenticated view
# TODO: Issue of authentication persist
def charging_stations(request, *args, **kwargs):
    context = {
        'charging_stations':
            ChargingStation.objects.all().prefetch_related('charging_point')
    }
    return render(request, 'charging_stations_logged.html', context=context)
