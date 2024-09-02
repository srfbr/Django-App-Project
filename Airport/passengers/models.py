from django.db import models
from flights.models import Flight

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passaport_number = models.CharField(max_length=20, unique=True, primary_key=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Booking(models.Model):
    booking_code = models.IntegerField(primary_key=True, default='')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)

    def __str__(self):
        return f"Booking: {self.passenger} on Flight {self.flight.flight_number}"