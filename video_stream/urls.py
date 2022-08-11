from django.shortcuts import render

from django.urls import path
from . import views

# app_name = 'watch'

urlpatterns = [
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('<int:pk>/', views.get_video, name='video'),
]