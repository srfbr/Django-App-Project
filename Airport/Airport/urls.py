from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include('flights.urls'), name='flights.urls'),
    path('passengers', include('passengers.urls'), name='passengers.urls')
]
