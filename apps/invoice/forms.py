from django import forms
from invoice.models import Invoice, InvoiceItem

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ('number', 'amount', 'vendor', 'date')
		widgets = {

		}

class InvoiceItemForm(forms.ModelForm):
	class Meta:
		model = InvoiceItem