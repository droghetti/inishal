from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import MainView
from django.conf import settings
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', MainView.as_view(), name='home'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # console area
    #(r'^console/accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'loginconsole.html'}),
    (r'^console/', include('console.urls')),

    (r'^photologue/', include('photologue.urls')),

    (r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)