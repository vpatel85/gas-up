from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    google_rating = models.PositiveIntegerField(blank=True, null=True)
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

