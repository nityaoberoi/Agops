from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from signup.forms import LoginForm, SignupForm


class HomeView(TemplateView):

    template_name = 'signup/home.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            view = LoginView()
            return view.dispatch(request)

        context = self.compute_context()
        return self.render_to_response(context)

    def compute_context(self):
        context = {}
        return context


class LoginView(TemplateView):

    form_class = LoginForm
    template_name = 'signup/login.html'

    def get(self, request, *args, **kwargs):
        self.form = self.form_class()
        context = self.compute_context()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
        if self.form.is_valid():
            return HttpResponseRedirect(reverse('home'))
        context = self.compute_context()
        return self.render_to_response(context)

    def compute_context(self):
        context = {}
        context['form'] = self.form_class()
        return context

class SignupView(TemplateView):

    from_class = SignupForm
    template_name = 'signup/signup.html'
