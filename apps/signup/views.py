from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from account.views import LoginView
from invoice.forms import InvoiceForm, InvoiceItemFormSet
from signup.forms import SignupForm


class HomeView(TemplateView):

    form_class = InvoiceForm
    formset_class = InvoiceItemFormSet
    template_name = 'signup/home.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            view = LoginView()
            return view.dispatch(request)

        self.form = self.form_class()
        self.formset = self.formset_class()
        context = self.compute_context()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        context = self.compute_context()
        return self.render_to_response(context)

    def compute_context(self):
        context = {}
        context['form'] = self.form
        context['formset'] = self.formset
        return context


class SignupView(TemplateView):

    form_class = SignupForm
    template_name = 'signup/signup.html'

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        context = self.compute_context()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        if self.form.is_valid():
            user = self.form.get_user()
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        context = self.compute_context()
        return self.render_to_response(context)

    def compute_context(self):
        context = {}
        context['form'] = self.form
        return context
