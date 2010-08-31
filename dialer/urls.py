from django.conf.urls.defaults import *
from dialer import views

urlpatterns = patterns('',
    url(
        r'^$',
        views.start,
        {},
        name='dialer_start',
    ),
    
    url(
        r'^dialed/$',
        views.dialed,
        {},
        name='dialer_dialed',
    ),
    
    url(
        r'^conf$',
        views.conf,
        {},
        name='dialer_conf',
    ),
    
    url(
        r'^conf/(?P<confid>\d+)/(?P<from_name>[\w\s]+)/(?P<to_name>[\w\s]+)/$',
        views.conf,
        {},
        name='dialer_confxml',
    ),
)
