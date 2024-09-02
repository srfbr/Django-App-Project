from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    city = models.CharField(max_length=100)
    country  = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country}"
    

class Airplane(models.Model):
    model = models.CharField(max_length=100, primary_key=True)
    capacity = models.IntegerField()

    def __str__(self): 
        return f"Model: {self.model}"
    

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, primary_key=True, default='')
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str(self):
        return f"Flight: {self.flight_number} | From: {self.departure_airport} | To: {self.arrival_airport}"