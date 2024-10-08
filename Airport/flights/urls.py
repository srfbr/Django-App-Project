from django.urls import path
from .api.views import FlightViewSet, AirplaneViewSet, AirportViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flights_manager', FlightViewSet)
app_name = 'flights_manager'

router.register(r'airplanes_manager', AirplaneViewSet)
app_name = 'airplanes_manager'

router.register(r'airports_manager', AirportViewSet)
app_name = 'airports_manager'

urlpatterns = [] + router.urls