from django.urls import path
from .api import views

urlpatterns = [
    path('pasengers_manager', views.passengers_manager, name='passengers_manager'),
    path('booking_manager/', views.booking_manager, name='bookings_manager')
]