from . import views
from django.conf.urls import url
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')