from django import forms
from django.forms.models import modelformset_factory

from invoice.models import Invoice, InvoiceItem


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('number', 'amount', 'vendor', 'date')
        widgets = {
            'number': forms.TextInput(attrs={'title': 'Invoice Number'}),
            'amount': forms.TextInput(attrs={'title': 'Total Amount'}),
            'vendor': forms.TextInput(attrs={'title': 'Vendor Name'}),
        }

InvoiceItemFormSet = modelformset_factory(InvoiceItem)
