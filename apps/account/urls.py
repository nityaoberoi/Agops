from django.conf.urls import patterns, url

from signup.views import LoginView


urlpatterns = patterns('',
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LoginView.as_view(), name='logout'),
)
