from django.urls import path 

from .views import *

urlpatterns = [
    path('tour/', virtual_tour, name='tour'),
    path('', home, name='home')
]
