from django.db import models

# Create your models here.
class ParkingLot(models.Model):
    lot_id = models.CharField(primary_key=True, max_length=6)
    lot_name = models.CharField(max_length=200)
    lot_hours = models.CharField(max_length=200)

class ParkingSpot(models.Model):
    spot_id = models.CharField(primary_key=True, max_length=6)
    lot_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    spot_number = models.CharField(max_length=6)
    spot_occupancy = models.CharField(max_length=1)
    spot_availabiliy = models.CharField(max_length=200)

#    def getLot_id(self):
#        return lot_id.lot_id

class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=6)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=20)
    postcode = models.CharField(max_length=6)

class Payment(models.Model):
    credit_card = models.CharField(primary_key=True, max_length=16)
    address = models.ForeignKey(Address, on_delete=models.CASCADE) 
    expiration_month = models.CharField(max_length=2)
    expiration_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)



