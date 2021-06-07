from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first),
    path('home', views.first),
    path('start', views.index),
    path('about', views.about)
]
