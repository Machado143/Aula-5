from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='home'),
    path('data-hora/', views.verDataHora, name='agora'),
]


