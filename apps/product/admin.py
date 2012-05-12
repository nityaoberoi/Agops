from django.contrib import admin
from product.models import RawProduct, RegularUnit

class RawProductAdmin(admin.ModelAdmin):
    pass

class RegularUnitAdmin(admin.ModelAdmin):
	pass

admin.site.register(RawProduct, RawProductAdmin)
admin.site.register(RegularUnit, RegularUnitAdmin)