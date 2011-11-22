from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'restaurants.views.homepage'),
    url(r'^restaurants/(?P<restaurants_id>\d+)/$', 'restaurants.views.detail'), 
          
    url(r'^admin/', include(admin.site.urls)),
)

