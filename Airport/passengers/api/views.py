from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from passengers.models import Passenger, Booking
from .serializers import PassengerSerializer, BookingSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer