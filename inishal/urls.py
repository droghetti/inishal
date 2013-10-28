from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import MainView
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', MainView.as_view(), name='home'),
    # url(r'^inishal/', include('inishal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)