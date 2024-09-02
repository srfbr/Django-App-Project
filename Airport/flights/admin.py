from django.contrib import admin
from .models import Airplane, Airport, Flight

admin.site.register(Airport)

admin.site.register(Airplane)

admin.site.register(Flight)