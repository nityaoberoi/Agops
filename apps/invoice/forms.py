from django import forms
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

class InvoiceItemForm(forms.ModelForm):
	class Meta:
		model = InvoiceItem
		fields = ('invoice_product', 'quantity', 'price')
		widgets = {
			'invoice_product': forms.TextInput(attrs={'title': 'Invoice Product'}),
		}