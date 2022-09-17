from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility

# Create your models here.

class user(models.Model):
   
    fullname = models.CharField(max_length=100)
    email_id = models.EmailField()
    password = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=12)
    lic_no =  models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

class booking(models.Model):

    booking_number = models.CharField(max_length=100)
    email_id =models.EmailField()
    veh_id = models.IntegerField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    from_destination = models.CharField(max_length=100)
    date_booked =models.DateField
    status = models.CharField(max_length=100)
    total_price = models.IntegerField()
    refund_price = models.FloatField(default=None, blank=True, null=True)
    diff_amount = models.FloatField(default=None, blank=True, null=True)
    additional_charge = models.IntegerField(default=None, blank=True, null=True)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)    
    