from django.contrib import admin
from .models import Feed_Post, Comment

# Register your models here.
admin.site.register(Feed_Post)
admin.site.register(Comment)

#superuser id:admin pw:1234