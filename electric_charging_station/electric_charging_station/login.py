from django import forms
from django.contrib.auth import authenticate, forms, login as auth_login
from django.shortcuts import render, redirect


def login(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session.set_expiry(86400)
            auth_login(request, user)
        return redirect('charging_stations_authenticated', permanent=True)
    if request.method == 'GET':
        return render(request, 'registration/login.html', context={'form': forms.AuthenticationForm()})
