from django.contrib import admin
from invoice.models import Invoice, InvoiceItem, InvoiceProduct, Brand


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline, ]


class InvoiceItemAdmin(admin.ModelAdmin):
    pass


class InvoiceProductAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(InvoiceProduct, InvoiceProductAdmin)
admin.site.register(Brand, BrandAdmin)
