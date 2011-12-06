from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'restaurants.views.homepage'),
    url(r'^restaurants/(?P<restaurants_id>\d+)/$', 'restaurants.views.detail'), 
    url(r'^cuisines/(?P<cuisines_id>\d+)/$', 'restaurants.views.cuisinedetail'),     
    url(r'^restaurant-type/(?P<restauranttype_id>\d+)/$', 'restaurants.views.restaurantdetail'), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ratings/(?P<rating_id>\d+)/$', 'restaurants.views.ratingdetail'),
)

