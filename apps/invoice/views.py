from django.views.generic.base import TemplateView

from invoice.forms import InvoiceForm, InvoiceItemForm


class InvoiceEntry(TemplateView):

    template_name = 'invoice/invoice_entry.html'
    form_class = InvoiceForm
    item_formclass = InvoiceItemForm

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

