from django.contrib import admin
from invoice.models import Invoice, InvoiceItem, InvoiceProduct

class InvoiceAdmin(admin.ModelAdmin):
    pass

class InvoiceItemAdmin(admin.ModelAdmin):
	pass

class InvoiceProductAdmin(admin.ModelAdmin):
	pass

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(InvoiceProduct, InvoiceProductAdmin)