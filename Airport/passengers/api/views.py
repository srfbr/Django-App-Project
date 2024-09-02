from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from passengers.models import Passenger, Booking
from .serializers import PassengerSerializer, BookingSerializer




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def passengers_manager(request):

    if request.method == 'GET':

        passengers = Passenger.objects.all()
        
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

            new_passenger = request.data
            
            serializer = PassengerSerializer(data=new_passenger)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':
            
        passaport_number = request.data['passaport_number']

        try:
            update_passenger = Passenger.objects.get(pk=passaport_number)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        print(request.data)
            
        serializer = PassengerSerializer(update_passenger, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
            
        try:
                
            passenger_to_delete = Passenger.objects.get(pk=request.data['passaport_number'])
            passenger_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def booking_manager(request):
    
    if request.method == 'GET':

        booking = Booking.objects.all()
        
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

            new_booking = request.data
            
            serializer = BookingSerializer(data=new_booking)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':
            
        booking_code = request.data['booking_code']

        try:
            update_booking = Booking.objects.get(pk=booking_code)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        print(request.data)
            
        serializer = BookingSerializer(update_booking, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
            
        try:
                
            booking_to_delete = Booking.objects.get(pk=request.data['booking_code'])
            booking_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)