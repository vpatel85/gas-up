from rest_framework import serializers
from django.contrib.auth.models import User
from restaurants.models import UserProfile, Restaurant, Comment, SubComment

class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = ('parent', 'comment')

class CommentSerializer(serializers.ModelSerializer):
    subcomment_set = SubCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = ('id', 'subcomment_set', 'restaurant', 'comment')

class UserSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer()
    class Meta:
        model = User
        fields = ('comment_set', 'username', 'first_name', 'last_name', 'email')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    visited = serializers.RelatedField(many=True)
    dislike = serializers.RelatedField(many=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'visited', 'dislike')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('url', 'name', 'google_rating', 'up_vote', 'down_vote', 'price_level', 'icon', 'created', 'updated', 'comment_set')
