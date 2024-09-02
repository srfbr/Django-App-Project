from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from flights.models import Flight, Airplane, Airport
from .serializers import FlightSerializer, AirplaneSerializer, AirportSerializer




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def flights_manager(request):

    if request.method == 'GET':

        flights = Flight.objects.all()
        
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

            new_flight = request.data
            
            serializer = FlightSerializer(data=new_flight)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':
            
        flight_number = request.data['flight_number']

        try:
            update_passenger = Flight.objects.get(pk=flight_number)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        print(request.data)
            
        serializer = FlightSerializer(update_passenger, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
            
        try:
                
            flight_to_delete = Flight.objects.get(pk=request.data['flight_number'])
            flight_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def airplanes_manager(request):
    
    if request.method == 'GET':

        airplanes = Airplane.objects.all()
        
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

            new_airplane = request.data
            
            serializer = AirplaneSerializer(data=new_airplane)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':
            
        model = request.data['model']

        try:
            update_airplane = Airplane.objects.get(pk=model)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        print(request.data)
            
        serializer = AirplaneSerializer(update_airplane, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
            
        try:
                
            airplane_to_delete = Airplane.objects.get(pk=request.data['model'])
            airplane_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def airports_manager(request):

    if request.method == 'GET':

        airports = Airport.objects.all()
        
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

            new_airport = request.data
            
            serializer = AirportSerializer(data=new_airport)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':
            
        name = request.data['name']

        try:
            update_airport = Airport.objects.get(pk=name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        print(request.data)
            
        serializer = AirportSerializer(update_airport, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
            
        try:
                
            airport_to_delete = Airport.objects.get(pk=request.data['name'])
            airport_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)