from django.conf.urls import patterns, url

from signup.views import LoginView, SignupView


urlpatterns = patterns('',
    url(r'^$', SignupView.as_view(), name='signup'),
    url(r'^login$', LoginView.as_view(), name='login'),
)
