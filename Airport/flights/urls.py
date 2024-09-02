from django.urls import path
from .api import views

urlpatterns = [
    path('flights_manager/', views.flights_manager, name='flights_manager'),
    path('airplanes_manager/', views.airplanes_manager, name='airplanes_manager'),
    path('airports_manager/', views.airports_manager, name='airports_manager')
]