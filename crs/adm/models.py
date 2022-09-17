from django.db.models.fields import IntegerField, NullBooleanField
from django.forms import ModelForm, Textarea
from django.db import models




# Create your models here.

class login(models.Model):
   
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class location(models.Model):

    pincode = models.IntegerField()
    l_name = models.CharField(max_length=100)


class vehicles(models.Model):
    
    vehicle_brand = models.CharField(max_length=30)
    l_name = models.CharField(max_length=100)
    vehicle_name = models.CharField(max_length=100)   
    vehicle_image = models.URLField()  
    price_per_day = models.IntegerField()
    fuel_type = models.CharField(max_length=100)  
    seating_capacity = models.CharField(max_length=100)  
    aircondition = models.CharField(max_length=100)  
    airbag = models.CharField(max_length=100)  
    vehicle_no = models.CharField(max_length=100)



   

class Meta:
    db_table = "admin"
    db_table = "location"   

