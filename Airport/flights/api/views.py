from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from flights.models import Flight, Airplane, Airport
from .serializers import FlightSerializer, AirplaneSerializer, AirportSerializer


class FlightViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['flight_number']

class AirplaneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['model']
        
class AirportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']