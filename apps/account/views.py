from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from signup.forms import LoginForm


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
        context['form'] = self.form_class()
        return context
