from django.contrib import admin

# Register your models here.
from .models import ParkingLot
from .models import ParkingSpot
from .models import Address
from .models import Payment

admin.site.register(ParkingLot)
admin.site.register(ParkingSpot)
admin.site.register(Address)
admin.site.register(Payment)

admin.site.site_header = "Parking Administration"


