from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey('vendor.Country', null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    #payment_terms = 

class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)