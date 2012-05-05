from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

class Invoice(models.Model):
    number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True)

class InvoiceItem(models.Model):
    product_number = models.ForeignKey('invoice.RawProduct')
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class RawProduct(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    brand = models.ForeignKey('invoice.Brand')
    shelf_life = models.PositiveSmallIntegerField(default=0)

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey('invoice.Country', null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    #payment_terms = 

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    #recipe = models.ManyToManyField()
    shelf_life = models.PositiveSmallIntegerField(default=0)

class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)