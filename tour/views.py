from http.client import HTTPResponse
from django.shortcuts import render

from .models import *

def home(request):
    tours_is_restored = Tour.objects.filter(is_restored=True)
    tours = Tour.objects.filter(is_restored=False)[:4]
    return render(request, 'tour/index.html', context={'title': 'Главная страница', 'tours_is_restored': tours_is_restored, 'tours': tours})
