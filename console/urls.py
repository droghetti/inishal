from django.conf.urls import patterns, url
from .views import MainView

urlpatterns = patterns('console.views',
    # console area
    url(regex='^$',
       view=MainView.as_view(),
       name='home'),
)

urlpatterns += patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'loginconsole.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/console/accounts/login/'}),
)