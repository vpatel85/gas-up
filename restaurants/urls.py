from django.conf.urls import patterns, include, url
from .views import SearchRestaurant, SearchResults

urlpatterns = patterns('restaurants.views',
        url(r'^search/', SearchRestaurant.as_view(), name='search_restaurant'),
        url(r'^results/', SearchResults.as_view(), name='search_results'),
)
