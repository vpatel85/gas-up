from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from rest_framework import routers
from restaurants.api.views import UserProfileViewSet, RestaurantViewSet, CommentViewSet, SubCommentViewSet

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'sub-comments', SubCommentViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gas_up.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/restaurants/list')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^restaurants/', include('restaurants.urls'), name='restaurants'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
