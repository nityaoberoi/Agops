from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect

from account.forms import LoginForm


class LoginView(TemplateView):

    form_class = LoginForm
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        context = self.compute_context()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        if self.form.login(request):
            return HttpResponseRedirect(reverse('home'))
        context = self.compute_context()
        return self.render_to_response(context)

    def compute_context(self):
        context = {}
        context['form'] = self.form
        return context


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request, request.user)
        return HttpResponseRedirect(reverse('login'))
