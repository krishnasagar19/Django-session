from django.contrib import admin

from charging_stations.models import ChargingStation, ChargingPoint

admin.site.register(ChargingStation)
admin.site.register(ChargingPoint)
