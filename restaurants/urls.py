from django.conf.urls import patterns, include, url
from .views import SearchRestaurant

urlpatterns = patterns('restaurants.views',
        url(r'^search/', SearchRestaurant.as_view(), name='search_restaurant'),
)
