from django.db import models

class Invoice(models.Model):
    number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vendor = models.ForeignKey('vendor.Vendor')
    date = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey('invoice.Invoice')
    invoice_product = models.ForeignKey('invoice.InvoiceProduct')
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class InvoiceProduct(models.Model):
    number = models.CharField(max_length=255)
    raw_product = models.ForeignKey('product.RawProduct')
    brand = models.ForeignKey('invoice.Brand')
    quantity = models.PositiveSmallIntegerField(default=0, help_text='Number of this unit. e.g.: 18oz -> 18')
    unit = models.ForeignKey('product.RegularUnit', help_text='Unit of this product. 18oz -> oz')

class Brand(models.Model):
    name = models.CharField(max_length=255)
