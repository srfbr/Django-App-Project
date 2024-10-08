from django.urls import path
from .api.views import PassengerViewSet, BookingViewSet
from rest_framework. routers import DefaultRouter

router = DefaultRouter()

router.register(r'passengers_manager', PassengerViewSet)
app_name = 'passenger_manager'
 
router.register(r'booking_manager', BookingViewSet)
app_name = 'booking_manager'


urlpatterns = [
    
] + router.urls