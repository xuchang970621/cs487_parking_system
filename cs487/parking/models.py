from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=6)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=20)
    postcode = models.CharField(max_length=6)
    
    def __str__(self):
        return self.line1 + ', ' + self.line2 + '\n' + self.city + ', ' + self.state + ', ' + self.postcode + '\n' + self.country + '\n'

class ParkingLot(models.Model):
    lot_id = models.CharField(primary_key=True, max_length=6)
    lot_name = models.CharField(max_length=200)
    lot_hours = models.CharField(max_length=200)
    lot_address = models.ForeignKey(Address, on_delete=models.CASCADE)

class ParkingSpot(models.Model):
    spot_id = models.CharField(primary_key=True, max_length=6)
    lot_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    spot_number = models.CharField(max_length=6)
    spot_occupancy = models.CharField(max_length=1)
    spot_availabiliy = models.CharField(max_length=200)
    spot_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booked_date = models.DateField(null=True, blank=True)
    booked_time = models.DateTimeField(null=True, blank=True)
    booked_minute = models.IntegerField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    license_plate = models.CharField(max_length=7, null=True, blank=True)
    class Meta:
        permissions = (("booked", "This parking spot is booked by this user"),)   
    def checkStatus(self):
        #occupied
        if self.booked_time > datetime.datetime.now() and self.booked_time < datetime.datetime.now() + timedelta(hours=24):
            return 'o'
        if self.end_time > datetime.datetime.now() and self.end_time < datetime.datetime.now() + timedelta(hours=24):
            return 'o'        
        #not occupied
        return 'n'
#    def getLot_id(self):
#        return lot_id.lot_id


class Payment(models.Model):
    credit_card = models.CharField(primary_key=True, max_length=16)
    address = models.ForeignKey(Address, on_delete=models.CASCADE) 
    expiration_month = models.CharField(max_length=2)
    expiration_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)



