from django.contrib import admin
from .models import Restaurant, Comment, SubComment, UserProfile

admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(UserProfile)
