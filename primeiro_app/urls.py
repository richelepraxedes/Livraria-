from django.contrib import admin
from django.urls import path
from primeiro_app import views

urlpatterns = [
    path('relogio/', views.data_e_hora),
    path('home/', views.home),
]
