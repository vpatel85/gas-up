from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import SearchRestaurant, SearchResults, AddRestaurant, RestaurantList, RestaurantDetail, SubCommentView, UserProfileView, RemoveRestaurantUser, AddRestaurantUser

urlpatterns = patterns('restaurants.views',
        url(r'^search/', login_required(SearchRestaurant.as_view()), name='search_restaurant'),
        url(r'^results/', login_required(SearchResults.as_view()), name='search_results'),
        url(r'^add/', login_required(AddRestaurant.as_view()), name='add_restaurant'),
        url(r'^list/', login_required(RestaurantList.as_view()), name='restaurant_list'),
        url(r'^(?P<pk>\d+)/', login_required(RestaurantDetail.as_view()), name='restaurant_detail'),
        url(r'^sub-comment/(?P<pk>\d+)/', login_required(SubCommentView.as_view()), name='sub-comment'),
        url(r'^user/(?P<pk>\d+)', login_required(UserProfileView.as_view()), name='user-profile'),
        url(r'^user-remove/(?P<pk>\d+)', login_required(RemoveRestaurantUser.as_view()), name='remove_restaurant_user'),
        url(r'^user-add/(?P<pk>\d+)', login_required(AddRestaurantUser.as_view()), name='add_restaurant_user'),
)
