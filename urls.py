from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'peoplepatcher.views.index', name='index'),
    
    url(r'^dialer/', include('dialer.urls'), name='dialer'),
    
    url(r'^autodialer/', include('autodialer.urls'), name='autodialer'),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
