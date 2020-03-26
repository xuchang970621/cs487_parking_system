from django.contrib import admin

# Register your models here.
from .models import ParkingLots
from .models import ParkingSpots
from .models import Address
from .models import Payment

admin.site.register(ParkingLots)
admin.site.register(ParkingSpots)
admin.site.register(Address)
admin.site.register(Payment)
