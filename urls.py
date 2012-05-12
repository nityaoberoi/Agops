from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'agops.views.home', name='home'),
    # url(r'^agops/', include('agops.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^404$', direct_to_template, {'template': "404.html"}, name='404'),
    url(r'^500$', direct_to_template, {'template': "500.html"}, name='500'),
)
if settings.LOCAL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)