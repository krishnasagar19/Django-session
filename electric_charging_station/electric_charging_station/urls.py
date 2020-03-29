"""electric_charging_station URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.shortcuts import redirect
from django.urls import path

import charging_stations.views as charging_stations_views

profile_redirct = lambda request: redirect('charging_stations_authenticated', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    url('accounts/profile/', profile_redirct),
    url('charging_stations', charging_stations_views.all_charging_stations, name='charging_stations'),
    url('charging_stations_authenticated', charging_stations_views.charging_stations,
        name='charging_stations_authenticated'),
]
