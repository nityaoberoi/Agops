from django.contrib import admin
from vendor.models import Vendor, Country

class VendorAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Country, CountryAdmin)
