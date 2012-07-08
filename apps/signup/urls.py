from django.conf.urls import patterns, url

from signup.views import SignupView


urlpatterns = patterns('',
    url(r'^$', SignupView.as_view(), name='signup'),
)
