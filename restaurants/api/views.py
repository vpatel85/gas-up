from rest_framework import viewsets
from .serializers import UserProfileSerializer, RestaurantSerializer, CommentSerializer, SubCommentSerializer
from restaurants.models import UserProfile, Restaurant, Comment, SubComment

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SubCommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer
