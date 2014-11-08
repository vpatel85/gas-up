from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    google_rating = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=1)
    up_vote = models.PositiveIntegerField(default=0)
    down_vote = models.PositiveIntegerField(default=0)
    price_level = models.PositiveIntegerField(blank=True, null=True)
    icon = models.URLField(null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def total_rating(self):
        return self.up_vote - self.down_vote

    def __unicode__(self):
        return '%s' % self.name

#abstract polymorphic model structure here to allow better comment relationship
class Comment(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    comment = models.TextField()

    created = models.DateTimeField(auto_now_add=True, blank=True)

class SubComment(models.Model):
    parent = models.ForeignKey(Comment)
    user = models.ForeignKey(User)
    comment = models.TextField()

    created = models.DateTimeField(auto_now_add=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    visited = models.ManyToManyField(Restaurant, related_name='visited_restaurants')
    dislike = models.ManyToManyField(Restaurant, related_name='disliked_restaurants')

